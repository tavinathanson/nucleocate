#!/usr/bin/env python27
"""
Given a genetic sequence as well as a start/end position, locate the
nucleotide at a particular position.

nucleocate.py <seq> <start_pos> <end_pos> <search_pos>
"""


import argparse
from textwrap import wrap


def nucleocate():
    parser = argparse.ArgumentParser(usage=__doc__)
    parser.add_argument('seq', nargs=1,
                        help='The genetic sequence')
    parser.add_argument('start_pos', nargs=1,
                        help='The starting position of the sequence')
    parser.add_argument('end_pos', nargs=1,
                        help='The ending position of the sequence')
    parser.add_argument('search_pos', nargs=1,
                        help='The search position')

    args = parser.parse_args()

    seq = ''.join(args.seq[0].split())
    start_pos = to_num(args.start_pos[0])
    end_pos = to_num(args.end_pos[0])
    search_pos = to_num(args.search_pos[0])

    index = start_pos - search_pos
    if index < 0:
        index = index * -1

    before = seq[:index]
    after = seq[index + 1:]
    output = before + '[' + seq[index] + ']' + after

    print output


def to_num(num_str):
    return int(''.join(char for char in num_str if char.isdigit()))


if __name__ == "__main__":
    nucleocate()

