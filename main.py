#!/usr/bin/env python2
"""Smart Todo app

Usage:
  main.py add <item>
  main.py del <item-number>
  main.py list
  main.py clear

Options:
  -h --help     Show this screen.
  --version     Show version.
"""

from docopt import docopt
from data_accessor import DataAccessor

import sys
import os

def main(argv):
    arguments =  docopt(__doc__, version='v0.0.1')

    todo_storage_file_name = os.path.join(os.path.expanduser('~'), ".todo.db")
    data_accessor = DataAccessor(todo_storage_file_name)

    if arguments['add']:
        data_accessor.add_task(arguments['<item>'])


    elif arguments['del']:
        data_accessor.delete_task(arguments['<item-number>'])

    elif arguments['list']:
        tasks = data_accessor.get_all_tasks()
        for i, line in tasks:
            print str(i) + ". " + line 

    elif arguments['clear']:
        data_accessor.clear_all_tasks()

if __name__ == '__main__':
    main(sys.argv)
