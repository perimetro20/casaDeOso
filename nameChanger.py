#!/usr/bin/env python

import fileinput
import os
import sys


filesToEdit = ['HOWTOUSE.md',
               'manage.py',
               'casa_de_oso/urls.py',
               'casa_de_oso/wsgi.py',
               'casa_de_oso/settings/base.py']

with fileinput.FileInput(filesToEdit, inplace=True) as file:
    for line in file:
        print(line.replace('casa_de_oso', sys.argv[1]), end='')


# Change the name of the main project folder
os.rename('casa_de_oso', sys.argv[1])
