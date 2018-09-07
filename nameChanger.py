#!/usr/bin/env python

import fileinput
import os
import sys


filesToEdit = ['HOWTOUSE.md',
               'manage.py',
               'hyrisa/urls.py',
               'hyrisa/wsgi.py',
               'hyrisa/settings/base.py']

with fileinput.FileInput(filesToEdit, inplace=True) as file:
    for line in file:
        print(line.replace('hyrisa', sys.argv[1]), end='')


# Change the name of the main project folder
os.rename('hyrisa', sys.argv[1])
