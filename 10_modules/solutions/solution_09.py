"""Solution 09 (bonus) -- A command line."""

import argparse


def build_parser():
    parser = argparse.ArgumentParser(prog="report", description="Summarise a sensor log.")
    parser.add_argument("path")  # positional, required
    parser.add_argument("--limit", type=float, default=85.0)  # converted for you
    parser.add_argument("--verbose", action="store_true")  # a flag: present or not
    return parser


parser = build_parser()

# Passing a list is how a parser is tested; with no argument it reads sys.argv.
args = parser.parse_args(["data/readings.csv", "--limit", "90"])
print(args.path, args.limit, args.verbose)
print(type(args.limit).__name__)

defaults = parser.parse_args(["data/readings.csv"])
print(defaults.limit, defaults.verbose)

try:
    parser.parse_args(["--limit", "abc", "x"])
except SystemExit as err:
    # argparse prints usage and exits the process rather than raising something
    # you can inspect. SystemExit is not an Exception -- module 09.
    print("SystemExit", err.code)
