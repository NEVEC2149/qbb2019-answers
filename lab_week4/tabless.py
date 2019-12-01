#!/usr/bin/env python3

import sys

for i, line in enumerate( open(sys.argv[1]) ):
    if i == 0:
        continue
    fields = line.rstrip("\n").split()
    