#!/usr/bin/env python
# encoding=utf-8

import os
import sys


sys.path.append(f'{os.path.dirname(__file__)}/..')

from amk.rfwd.__init__ import main
# from amk.rename_files_with_date.__init__ import main


if __name__ == '__main__':
    main()
