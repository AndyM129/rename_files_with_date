#!/usr/bin/env python
# encoding=utf-8

import re
import random
import exifread

from .logger import *

# 支持的图片后缀
image_exts = {'jpg', 'bmp', 'png', 'jpeg', 'rgb', 'tif', 'heic'}


# 相关说明
def rename_tips():
    print_info(f'## 图标说明')
    print_info()
    print_info(f'> 🈚️ 表示路径不存在')
    print_info(f'> 📁 表示文件夹')
    print_info(f'> 🏞  表示图片')
    print_info(f'> ⏭️  表示跳过，例如该文件名称 无需重命名')
    print_info(f'> ✅ 表示处理成功')
    print_info()


# 将文件重命名
def rename_with_date(path):
    if path is None:
        print_error(f'❌ 请输入 path')
        print_info()
        parser.print_help()
        print_info()
        parser.exit()

    print_info(f'## 开始重命名')
    print_info()
    _rename_with_date(path)


# 将照片重命名
def _rename_with_date(path):
    # 异常处理
    if path is None or not os.path.exists(path):
        print_error(f'🈚️ {path}')
        return

    # 目录，则遍历其下的文件
    if os.path.isdir(path):
        for home, dirs, files in os.walk(path):
            print_verbose()
            print_verbose(f'📁 {home}')
            print_debug(f' ┣━ home = {home}')
            print_debug(f' ┣━ dirs = {dirs}')
            print_debug(f' ┗━ files = {files if len(files) < 20 else len(files)}个')
            for file in files:
                if file == '.DS_Store': continue
                _rename_with_date(f'{home}/{file}')
        return

    print_verbose()
    print_verbose(f'🏞  {path}')

    # 若不要求所有：若文件名 符合目标的命名格式，则跳过
    if not args.all:
        already_renamed = re.match(r'\d{4}-\d{2}-\d{2} \d{2}\.\d{2}\.\d{3}(_.*)?\.\w+', os.path.basename(path), re.M | re.I)
        if already_renamed:
            print_info(f'⏭️  {path}')
            return

    # 文件时间：读取拍摄时间（仅限图片）、创建时间、修改时间
    print_verbose(f' ┣━ 获取日期')

    ctime = os.path.getctime(path)
    print_verbose(f' ┃   ┣━ getctime: {ctime:.0f} => {time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(ctime))}')

    modifi_time = os.path.getmtime(path)
    print_verbose(f' ┃   ┣━ getmtime: {modifi_time:.0f} => {time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(modifi_time))}')

    file_stat = str(os.popen(f'stat -r "{path}"').readlines()[0]).strip()
    print_verbose(f' ┃   ┣━ stat -r: {file_stat}')

    file_stat_components = str(file_stat).split(' ')
    print_verbose(f' ┃   ┃   ┣━ components: {file_stat_components}')

    stat_create_time = float(file_stat_components[11])
    print_verbose(f' ┃   ┃   ┗━ create_time: {stat_create_time:.0f} => {time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(stat_create_time))}')

    img_read = open(path, 'rb')
    img_exif = exifread.process_file(img_read)
    print_verbose(f' ┃   ┣━ exifread')
    for img_exif_key, img_exif_value in img_exif.items():
        if 'date' not in img_exif_key.lower() and '日期' not in img_exif_key: continue
        print_verbose(f' ┃   ┃   ┣━ {img_exif_key}: {img_exif_value}')

    take_date_time = img_exif.get('EXIF DateTimeDigitized')
    if take_date_time is not None: take_date_time = str(take_date_time)[:19]
    take_time = time.mktime(time.strptime(take_date_time, "%Y:%m:%d %H:%M:%S")) if take_date_time is not None else None
    print_verbose(f' ┃   ┃   ┗━ 拍摄日期: {int(take_time) if take_time else None} => {take_date_time}')

    create_time = min(ctime, modifi_time, stat_create_time, take_time) if take_time else min(ctime, modifi_time, stat_create_time)
    print_verbose(f' ┃   ┗━ 最终的文件时间: {time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(create_time))}')

    # 准备变量
    dir = '/'.join(path.split('/')[:-1])
    name = path.split('/')[-1].strip()
    print_debug(f' ┣━ 提取文件名中的有效文本: {name}')

    name = name.split('】')[-1].strip()
    print_debug(f' ┃   ┣━ => {name}')

    name_components = re.match(r'^[a-zA-Z0-9_-]+( \d{2}\.\d{2}\.\d{3}_?)?', name, re.M | re.I)
    if name_components: name = name.replace(name_components.group(), '').strip()
    print_debug(f' ┃   ┣━ => {name}')

    name = name[:(name.find('.'))].strip()
    print_debug(f' ┃   ┣━ => {name}')

    if re.match(r'^\d+', name, re.M | re.I): name = ''
    print_debug(f' ┃   ┗━ => {name}')

    ext = path.split('.')[-1]
    create_time_str = time.strftime('%Y-%m-%d %H.%M', time.localtime(create_time))
    new_path = f'{dir}/{create_time_str}.{random.randint(100, 999)}{"_" + name if len(name) > 0 else ""}.{ext}'
    while os.path.isfile(new_path):
        new_path = f'{dir}/{create_time_str}.{random.randint(100, 999)}.{ext}'
        print_verbose(f'\t文件已存在，重新生成文件名：{new_path}')

    print_success(f'{" ┗━ 执行重命名: " if args.verbose else "✅ "}{path} ➡️  {new_path}')

    # 执行重命名
    if args.list is False:
        os.rename(path, new_path)


def main():
    try:
        print_info(f'# 用文件日期将文件重命名')
        print_info()
        rename_tips()
        rename_with_date(args.path)
        print_success()
        print_success(f'## 完成')
        print_success()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
