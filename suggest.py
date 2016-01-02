#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import datetime

if __name__ == '__main__':
    filename = 'data/suggestions/' + \
        os.getenv('NICKNAME') + '_' + \
        datetime.datetime.now().strftime("%Y-%m-%d-%H:%m")
    f = open(filename, 'w')
    content = ' '.join(sys.argv[1:])
    if sys.argv[1:] != []:
        f.write(content)
        print('Suggestion added.')
    f.close()
