#!/usr/bin/env python3

from random import getrandbits
import sys

if len(sys.argv) < 2:
    print('Usage: randomcase <string>', file=sys.stderr)
    sys.exit(1)

s = ' '.join(sys.argv[1:])
print(''.join(c.upper() if getrandbits(1) else c.lower() for c in s))
