#!/usr/bin/env python
# encoding=utf-8

import argparse
import textwrap
from .consts import *


# 命令行参数解析
parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    prog=NAME,
    prefix_chars='-+',
    description=textwrap.dedent(
        f'{NAME} —— {DESC}'
        + f'\n' + '-' * 80
        + f'\nSHORTCUT: {SHORTCUT}'
        + f'\nVERSION: {VERSION}'
        + f'\nUPDATE_TIME: {UPDATE_TIME}'
        + f'\nAUTHOR_NAME: {AUTHOR_NAME}'
        + f'\nAUTHOR_EMAIL: {AUTHOR_EMAIL}'
        + f'\nAUTHOR_URL: {AUTHOR_URL}'
        + f'\nGIT_URL: {GIT_URL}'
        + f'\nPIP_URL: {PIP_URL}'
        + f'\n' + '=' * 80
    ),
)

# 一级参数
parser.add_argument('path', nargs='?', help='待重命名的「文件/目录」的路径')
parser.add_argument('-d', '--debug', action='store_true', help='启用调试模式')
parser.add_argument('-v', '--verbose', action='store_true', help='显示详细日志')
parser.add_argument('-V', '--version', action='store_true', help='查看当前版本号')
parser.add_argument('-l', '--list', action='store_true', help='仅列表显示可能的处理，但不执行具体操作，以便检查')
parser.add_argument('-a', '--all', action='store_true', help='处理所有文件，即便文件名是已经符合目标命名')

# 解析命令
args = parser.parse_args()
