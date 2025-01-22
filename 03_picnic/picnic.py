#!/usr/bin/env python3
"""
Author : sgb <sgb@localhost>
Date   : 2025-01-20
Purpose: Picnic game
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        action='store_true',
                        help='Sort the items')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.item
    if args.sorted:
        items.sort()

    if len(items) == 1:
        print(f"You are bringing {''.join(items)}.")
    elif len(items) == 2:
        print(f"You are bringing {' and '.join(items)}.")
    elif len(items) > 2:
        lastitem = items.pop()
        print(f"You are bringing {', '.join(items)}, and {lastitem}.")
        

# --------------------------------------------------
if __name__ == '__main__':
    main()
