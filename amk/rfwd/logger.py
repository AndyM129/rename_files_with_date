#!/usr/bin/env python
# encoding=utf-8

import sys
from colorama import *
from .arg_parse import *


# 时间
def debug_time():
    time_str = (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    return f'[{time_str}] ' if args.debug else ''


# 输出信息：NOTSET
def print_noset(string='', end='\n'):
    print(debug_time() + string, end=end)


# 输出信息：DEBUG
def print_debug(string='', end='\n'):
    print(f'{Fore.LIGHTBLACK_EX}{Style.BRIGHT}{debug_time() + string}{Style.RESET_ALL}', end=end) if args.debug else None


# 输出信息：VERBOSE
def print_verbose(string='', end='\n'):
    print(f'{Fore.WHITE}{debug_time() + string}{Style.RESET_ALL}', end=end) if args.verbose else None


# 输出信息：INFO
def print_info(string='', end='\n'):
    print(f'{Fore.LIGHTCYAN_EX}{debug_time() + string}{Style.RESET_ALL}', end=end)


# 输出信息：WARNING
def print_warning(string='', end='\n'):
    print(f'{Fore.LIGHTYELLOW_EX}{debug_time() + string}{Style.RESET_ALL}', end=end)


# 输出信息：SUCCESS
def print_success(string='', end='\n'):
    print(f'{Fore.LIGHTGREEN_EX}{debug_time() + string}{Style.RESET_ALL}', end=end)


# 输出信息：ERROR
def print_error(string='', end='\n'):
    print(f'{Fore.LIGHTRED_EX}{debug_time() + string}{Style.RESET_ALL}', end=end)


# 输出信息：FATAL
def print_fatal(string='', end='\n', code=1):
    print(f'{Fore.LIGHTRED_EX}{debug_time() + Style.BRIGHT}{string}{Style.RESET_ALL}', end=end)
    if code is not None:
        sys.exit(code)


# 执行Shell 并打印命令、结果
def os_system(command, auto_exit=True):
    print_verbose()
    print_verbose(f'$ {command}')
    print_verbose()
    res = os.system(command)
    parser.exit() if res != 0 and auto_exit else None
    return res


# 输出信息：测试
def test_print():
    print_noset(f'[noset] This is {NAME}({VERSION})')
    print_debug(f'[debug] This is {NAME}({VERSION})')
    print_verbose(f'[verbose] This is {NAME}({VERSION})')
    print_info(f'[info] This is {NAME}({VERSION})')
    print_warning(f'[warning] This is {NAME}({VERSION})')
    print_success(f'[success] This is {NAME}({VERSION})')
    print_error(f'[error] This is {NAME}({VERSION})')
    print_fatal(f'[fatal] This is {NAME}({VERSION})')
    os_system(f'pwd')


# ========================================================= 打印内置常量 ============================================================
for info in parser.description.split('\n')[:-1]: print_debug(info)
print_debug()

# ========================================================= 打印内置常量 ============================================================
print_debug(f' Const '.center(120, '='))
print_debug(f'TIMESTAMP = {TIMESTAMP}')
print_debug(f'DATE_TIME = {DATE_TIME}')
print_debug(f'DATE_STAMP = {DATE_STAMP}')
print_debug(f'FILE = {FILE}')
print_debug(f'DIR = {DIR}')
print_debug(f'BASENAME = {BASENAME}')
print_debug(f'BASENAME_WITHOUT_SUFFIX = {BASENAME_WITHOUT_SUFFIX}')
print_debug(f'BASENAME_SUFFIX = {BASENAME_SUFFIX}')
print_debug()

# ========================================================= 打印命令行参数 ============================================================
print_debug(f' Command '.center(120, '='))
if args.debug is True: args.verbose = True
print_debug(f'$ {NAME} {" ".join(sys.argv[1:])}')
print_debug()

print_debug(f' Parsing Args '.center(120, '='))
for key, value in vars(parser.parse_args()).items():
    print_debug(f'{key} = {value}')
print_debug('\n' + '=' * 120 + '\n')
print_debug()
