#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

if len(sys.argv) > 1:
    print("https://www.startpage.com/do/search?q=" + "+".join(sys.argv[1:]))
