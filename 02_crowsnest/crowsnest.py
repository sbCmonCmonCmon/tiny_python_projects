#!/usr/bin/env python3
"""
Author : Scott
Date   : 2025-01-20
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word')

   
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Main"""

    args = get_args()
    word = args.word
    char = word[0].lower()
    article = 'an' if char in 'aeiou' else 'a'
    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')
    

# --------------------------------------------------
if __name__ == '__main__':
    main()
