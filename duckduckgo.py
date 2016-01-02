#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

if len(sys.argv) > 1:
    print("https://duckduckgo.com/?q=" + "+".join(sys.argv[1:]))
