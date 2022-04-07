#!/usr/bin/env python
# encoding=utf-8

import os, sys, time, random
import argparse
import re

from colorama import *
import exifread


# =========================================== COPYRIGHT ===========================================
__NAME__ = 'rpwd'  # 脚本名称
__FULL_NAME__ = 'rename_photos_with_date'  # 脚本名称
__DESC__ = 'Rename Photos With Date'  # 脚本名称
__VERSION__ = '0.1.2'  # 脚本版本
__UPDATE_TIME__ = '2022/04/07'  # 最近的更新时间
__AUTHOR_NAME__ = 'Andy Meng'  # 作者
__AUTHOR_EMAIL__ = 'andy_m129@163.com'  # 作者邮箱
__URL__ = 'https://github.com/AndyM129/rename_photos_with_date'  # 网址

# =========================================== GLOBAL CONST ===========================================
__TIMESTAMP__ = int(time.time())  # 当前时间戳，eg. 1617351251
__DATE_TIME__ = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(__TIMESTAMP__))  # 当前时间，eg. 2021-04-02 16:14:11
__DATE_STAMP__ = time.strftime('%Y%m%d%H%M%S', time.localtime(__TIMESTAMP__))  # 当前时间戳，eg. 20210402161411
__FILE__ = __file__  # 当前文件路径
__DIR__ = os.getcwd()  # 当前的文件目录
__BASENAME__ = os.path.basename(__file__)  # 当前脚本的文件名
__BASENAME_WITHOUT_SUFFIX__ = __BASENAME__.split('.')[0]  # 文件名（不含后缀）
__BASENAME_SUFFIX__ = __BASENAME__.split('.')[1]  # 文件后缀


# =========================================== RPWD ===========================================


class RPWD:
    # 支持的图片后缀
    image_exts = {'jpg', 'bmp', 'png', 'jpeg', 'rgb', 'tif', 'heic'}


    # 初始化
    def __init__(self):
        self.parsing_args()
        self.print_version_if_needed()
        self.print_info(f'# 重命名照片')
        self.print_info()
        self.photo_rename_tips()
        self.photo_rename_with_date(self.args.path)
        self.print_success()
        self.print_success(f'## 完成')
        self.print_success('\n')


    # 解析命令行参数
    def parsing_args(self):
        self.parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            prog=__NAME__,
            prefix_chars='-+',
            description=__DESC__,
        )
        self.parser.add_argument('path', nargs='?', help='待重命名的「文件/目录」的路径')
        self.parser.add_argument('-d', '--debug', action='store_true', help='启用调试模式')
        self.parser.add_argument('-v', '--verbose', action='store_true', help='显示详细日志')
        self.parser.add_argument('-V', '--version', action='store_true', help='查看当前版本号')
        self.parser.add_argument('-l', '--list', action='store_true', help='仅列表显示可能的处理，但不执行具体操作，以便检查')
        self.args = self.parser.parse_args()

        self.print_debug(f' Const '.center(120, '='))
        self.print_debug(f'__TIMESTAMP__ = {__TIMESTAMP__}')
        self.print_debug(f'__DATE_TIME__ = {__DATE_TIME__}')
        self.print_debug(f'__DATE_STAMP__ = {__DATE_STAMP__}')
        self.print_debug(f'__FILE__ = {__FILE__}')
        self.print_debug(f'__DIR__ = {__DIR__}')
        self.print_debug(f'__BASENAME__ = {__BASENAME__}')
        self.print_debug(f'__BASENAME_WITHOUT_SUFFIX__ = {__BASENAME_WITHOUT_SUFFIX__}')
        self.print_debug(f'__BASENAME_SUFFIX__ = {__BASENAME_SUFFIX__}')
        self.print_debug()

        self.print_debug(f' Command '.center(120, '='))
        if self.args.debug is True: self.args.verbose = True
        self.print_debug(f'$ {__NAME__} {" ".join(sys.argv[1:])}')
        self.print_debug()

        self.print_debug(f' Parsing Args '.center(120, '='))
        for key, value in vars(self.parser.parse_args()).items():
            self.print_debug(f'{key} = {value}')
        self.print_debug('\n' + '=' * 120 + '\n')


    # 按需输出当前版本号
    def print_version_if_needed(self):
        if self.args.version is False: return
        self.print_info(__VERSION__)
        sys.exit()


    # 相关说明
    def photo_rename_tips(self):
        self.print_info(f'## 图标说明')
        self.print_info()
        self.print_info(f'> 🈚️ 表示路径不存在')
        self.print_info(f'> 📁 表示文件夹')
        self.print_info(f'> 🏞  表示图片')
        self.print_info(f'> ⏭️  表示跳过，例如该文件名称 无需重命名')
        self.print_info(f'> ✅ 表示处理成功')
        self.print_info()


    # 将照片重命名
    def photo_rename_with_date(self, path):
        if path is None:
            self.print_error(f'❌ 请输入 path')
            self.print_info()
            self.parser.print_help()
            self.print_info()
            sys.exit()

        self.print_info(f'## 开始重命名')
        self.print_info()
        self._photo_rename_with_date(path)


    # 将照片重命名
    def _photo_rename_with_date(self, path):
        # 异常处理
        if path is None or not os.path.exists(path):
            self.print_error(f'🈚️ {path}')
            return

        # 目录，则遍历其下的文件
        if os.path.isdir(path):
            for home, dirs, files in os.walk(path):
                self.print_verbose()
                self.print_verbose(f'📁 {home}')
                self.print_debug(f' ┣━ home = {home}')
                self.print_debug(f' ┣━ dirs = {dirs}')
                self.print_debug(f' ┗━ files = {files if len(files) < 20 else len(files)}个')
                for file in files:
                    if file == '.DS_Store': continue
                    ext = file.split('.')[-1]
                    if ext.lower() not in self.image_exts:
                        self.print_verbose()
                        self.print_verbose(f'❓ {home}/{file}')
                        continue
                    self._photo_rename_with_date(f'{home}/{file}')
            return

        # 图片文件：若文件名 符合目标的命名格式，则跳过
        self.print_verbose()
        self.print_verbose(f'🏞  {path}')
        already_renamed = re.match(r'\d{8,}\.\d{3}\.\w+', os.path.basename(path), re.M | re.I)
        if already_renamed:
            self.print_info(f'⏭️  {path}')
            return

        # 图片文件：读取拍摄时间（用创建时间 兜底）
        img_read = open(path, 'rb')
        img_exif = exifread.process_file(img_read)
        take_date_time = img_exif.get('EXIF DateTimeDigitized')
        self.print_verbose(f' ┣━ 拍摄日期：{take_date_time}')
        modifi_time = os.path.getmtime(path)
        self.print_verbose(f' ┣━ 修改日期：{time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(modifi_time))}')
        create_time = os.path.getctime(path)
        self.print_verbose(f' ┣━ 创建日期：{time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(create_time))}')
        if take_date_time is not None:
            take_time = time.strptime(str(take_date_time), "%Y:%m:%d %H:%M:%S")
        else:
            take_time = time.localtime(create_time)

        # 准备变量
        dir = '/'.join(path.split('/')[:-1])
        name = path.split('/')[-1]
        ext = name.split('.')[-1]
        take_time_str = time.strftime('%Y%m%d%H%M', take_time)
        new_path = f'{dir}/{take_time_str}.{random.randint(100, 999)}.{ext}'
        while os.path.isfile(new_path):
            new_path = f'{dir}/{take_time_str}.{random.randint(100, 999)}.{ext}'
            self.print_verbose(f'\t文件已存在，重新生成文件名：{new_path}')

        self.print_success(f'{" ┗━ " if self.args.verbose else "✅ "}{path} => {new_path}')

        # 执行重命名
        if self.args.list is False:
            os.rename(path, new_path)


    # 时间
    def debug_time(self):
        time_str = (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        return f'[{time_str}] ' if self.args.debug else ''


    # 输出信息：NOTSET
    def print_noset(self, string='', end='\n'):
        print(self.debug_time() + string, end=end)


    # 输出信息：DEBUG
    def print_debug(self, string='', end='\n'):
        print(f'{Fore.LIGHTBLACK_EX}{Style.BRIGHT}{self.debug_time() + string}{Style.RESET_ALL}', end=end) if self.args.debug else None


    # 输出信息：VERBOSE
    def print_verbose(self, string='', end='\n'):
        print(f'{Fore.WHITE}{self.debug_time() + string}{Style.RESET_ALL}', end=end) if self.args.verbose else None


    # 输出信息：INFO
    def print_info(self, string='', end='\n'):
        print(f'{Fore.LIGHTCYAN_EX}{self.debug_time() + string}{Style.RESET_ALL}', end=end)


    # 输出信息：WARNING
    def print_warning(self, string='', end='\n'):
        print(f'{Fore.LIGHTYELLOW_EX}{self.debug_time() + string}{Style.RESET_ALL}', end=end)


    # 输出信息：SUCCESS
    def print_success(self, string='', end='\n'):
        print(f'{Fore.LIGHTGREEN_EX}{self.debug_time() + string}{Style.RESET_ALL}', end=end)


    # 输出信息：ERROR
    def print_error(self, string='', end='\n'):
        print(f'{Fore.LIGHTRED_EX}{self.debug_time() + string}{Style.RESET_ALL}', end=end)


    # 输出信息：FATAL
    def print_fatal(self, string='', end='\n', code=1):
        print(f'{Fore.LIGHTRED_EX}{self.debug_time() + Style.BRIGHT}{string}{Style.RESET_ALL}', end=end)
        if code is not None:
            sys.exit(code)


    # 输出信息：测试
    def test_print(self):
        self.print_noset(f'[noset] This is {__NAME__}({__VERSION__})')
        self.print_debug(f'[debug] This is {__NAME__}({__VERSION__})')
        self.print_verbose(f'[verbose] This is {__NAME__}({__VERSION__})')
        self.print_info(f'[info] This is {__NAME__}({__VERSION__})')
        self.print_warning(f'[warning] This is {__NAME__}({__VERSION__})')
        self.print_success(f'[success] This is {__NAME__}({__VERSION__})')
        self.print_error(f'[error] This is {__NAME__}({__VERSION__})')
        self.print_fatal(f'[fatal] This is {__NAME__}({__VERSION__})')


def main():
    RPWD()


if __name__ == '__main__':
    main()
