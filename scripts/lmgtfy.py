#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

if len(argv) > 1:
    print("http://lmgtfy.com/?q=" + "+".join(argv[1:]))
