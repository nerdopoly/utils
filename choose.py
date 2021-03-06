#!/usr/bin/env python3

"""Select random items from a list."""

from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import sys
import random

parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter,
                        description=__doc__)
parser.add_argument('-n', default=1, type=int, dest='num',
                    help='number of items to choose')
parser.add_argument('-s', '--shuffle', action='store_true', dest='shuffle',
                    help='shuffle items (i.e. choose all of them)')
parser.add_argument('items', nargs='+', help='items to choose from')
args = parser.parse_args()


def error(*values, code=1, **kwargs):
    """Print error message and then exit with error code."""
    print(parser.prog + ': error:', *values, file=sys.stderr, **kwargs)
    sys.exit(code)


if args.shuffle:
    args.num = len(args.items)

if args.num < 1:
    error('must choose at least 1 item')

if args.num > len(args.items):
    unit = 'item' if args.num == 1 else 'items'
    error("can't choose", args.num, unit, 'from a list of', len(args.items))

random.shuffle(args.items)
print('\n'.join(args.items[:args.num]))
