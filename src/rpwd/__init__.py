#!/usr/bin/env python
# encoding=utf-8

import os, sys, time, datetime, random
import argparse, textwrap
from colorama import *
import exifread


# =========================================== COPYRIGHT ===========================================
__NAME__ = 'rpwd'  # 脚本名称
__DESC__ = 'Rename Photos With Date'  # 脚本名称
__VERSION__ = '0.1.0'  # 脚本版本
__UPDATE_TIME__ = '2022/04/07'  # 最近的更新时间
__AUTHOR_NAME__ = 'Andy Meng'  # 作者
__AUTHOR_EMAIL__ = 'andy_m129@163.com'  # 作者邮箱
__URL__ = ''  # 说明文档

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

    # 初始化
    def __init__(self):
        self._parsing_args()


    # 解析命令行参数
    def _parsing_args(self):
        self.parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            prog=__NAME__,
            prefix_chars='-+',
            description=__DESC__,
        )
        self.parser.add_argument('path', help='待重命名的「文件/目录」的路径')
        self.parser.add_argument('-d', '--debug', action='store_true', help='启用调试模式')
        self.parser.add_argument('-v', '--verbose', action='store_true', help='显示详细日志')
        self.args = self.parser.parse_args()

        self._print_debug(f' Const '.center(120, '='))
        self._print_debug(f'__TIMESTAMP__ = {__TIMESTAMP__}')
        self._print_debug(f'__DATE_TIME__ = {__DATE_TIME__}')
        self._print_debug(f'__DATE_STAMP__ = {__DATE_STAMP__}')
        self._print_debug(f'__FILE__ = {__FILE__}')
        self._print_debug(f'__DIR__ = {__DIR__}')
        self._print_debug(f'__BASENAME__ = {__BASENAME__}')
        self._print_debug(f'__BASENAME_WITHOUT_SUFFIX__ = {__BASENAME_WITHOUT_SUFFIX__}')
        self._print_debug(f'__BASENAME_SUFFIX__ = {__BASENAME_SUFFIX__}')
        self._print_debug()

        self._print_debug(f' Command '.center(120, '='))
        self._print_debug(f'$ {__NAME__} {" ".join(sys.argv[1:])}')
        self._print_debug()

        self._print_debug(f' Parsing Args '.center(120, '='))
        for key, value in vars(self.parser.parse_args()).items():
            self._print_debug(f'{key} = {value}')
        self._print_debug()


    # 输出信息：NOTSET
    @staticmethod
    def _print_noset(string='', end='\n'):
        print(string, end=end)


    # 输出信息：DEBUG
    def _print_debug(self, string='', end='\n'):
        print(f'{Fore.LIGHTBLACK_EX}{Style.BRIGHT}{string}{Style.RESET_ALL}', end=end) if self.args.debug else None


    # 输出信息：VERBOSE
    def _print_verbose(self, string='', end='\n'):
        print(f'{Fore.WHITE}{string}{Style.RESET_ALL}', end=end) if self.args.verbose else None


    # 输出信息：INFO
    @staticmethod
    def _print_info(string='', end='\n'):
        print(f'{Fore.LIGHTCYAN_EX}{string}{Style.RESET_ALL}', end=end)


    # 输出信息：WARNING
    @staticmethod
    def _print_warning(string='', end='\n'):
        print(f'{Fore.LIGHTYELLOW_EX}{string}{Style.RESET_ALL}', end=end)


    # 输出信息：SUCCESS
    @staticmethod
    def _print_success(string='', end='\n'):
        print(f'{Fore.LIGHTGREEN_EX}{string}{Style.RESET_ALL}', end=end)


    # 输出信息：ERROR
    @staticmethod
    def _print_error(string='', end='\n'):
        print(f'{Fore.LIGHTRED_EX}{string}{Style.RESET_ALL}', end=end)


    # 输出信息：FATAL
    @staticmethod
    def _print_fatal(string='', end='\n', code=1):
        print(f'{Fore.LIGHTRED_EX}{Style.BRIGHT}{string}{Style.RESET_ALL}', end=end)
        if code is not None:
            sys.exit(code)


    # 输出信息：测试
    def _test_print(self):
        self._print_noset(f'[noset] This is {__NAME__}({__VERSION__})')
        self._print_debug(f'[debug] This is {__NAME__}({__VERSION__})')
        self._print_verbose(f'[verbose] This is {__NAME__}({__VERSION__})')
        self._print_info(f'[info] This is {__NAME__}({__VERSION__})')
        self._print_warning(f'[warning] This is {__NAME__}({__VERSION__})')
        self._print_success(f'[success] This is {__NAME__}({__VERSION__})')
        self._print_error(f'[error] This is {__NAME__}({__VERSION__})')
        self._print_fatal(f'[fatal] This is {__NAME__}({__VERSION__})')


def main():
    RPWD()


if __name__ == '__main__':
    main()
