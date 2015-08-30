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

import sys
import os

def main(argv):
    arguments =  docopt(__doc__, version='v0.0.1')

    todo_storage_file_name = os.path.join(os.path.expanduser('~'), ".todo")

    if arguments['add']:
        with open(todo_storage_file_name, "a") as todo_storage_file:
            todo_storage_file.write(arguments['<item>'] + '\n')
            todo_storage_file.close()

    elif arguments['del']:
        with open(todo_storage_file_name, "r") as todo_storage_file:
            items = enumerate(todo_storage_file.readlines(), start=1)
            todo_storage_file.close()

            with open(todo_storage_file_name, "w") as todo_storage_file:
                for i, line in items:
                    if i != int(arguments['<item-number>']):
                        todo_storage_file.write(line)
                todo_storage_file.close()

    elif arguments['list']:
        with open(todo_storage_file_name, "r") as todo_storage_file:
            for i, line in enumerate(todo_storage_file.readlines(), start=1):
                print str(i) + ". " + line ,
            todo_storage_file.close()

    elif arguments['clear']:
        with open(todo_storage_file_name, "w") as todo_storage_file:
            todo_storage_file.close()

if __name__ == '__main__':
    main(sys.argv)
