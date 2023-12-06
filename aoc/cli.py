import argparse
import datetime

import sys

from aoc.core import generate_template, fetch_input
from aoc.utils import set_session_token


def main():
    parser = argparse.ArgumentParser(
        prog=__package__,
        description="A small helper package for streamlining Advent of Code tasks",
    )

    parser.add_argument(
        "year",
        type=int,
        help="The AoC year you want to work with.",
        nargs="?",
        default=datetime.datetime.now().year,
    )
    parser.add_argument(
        "day",
        type=int,
        nargs="?",
        help="The AoC day you want to work with.",
        default=datetime.datetime.now().day,
    )
    parser.add_argument(
        "-c",
        "--create",
        action="store_true",
        help="Create a new python file to solve a particular year and day's puzzle.",
    )
    parser.add_argument(
        "-f",
        "--fetch",
        action="store_true",
        help="Fetch your input for a given year and day.",
    )
    parser.add_argument(
        "--set-token", help="Set your session token for communicating with AoC servers."
    )

    args = parser.parse_args()

    if args.year < 2015:
        print("The AoC year cannot be earlier than 2015!")
        sys.exit(1)

    if args.set_token:
        set_session_token(args.set_token)

    if args.create:
        generate_template(str(args.year), str(args.day))

    if args.fetch:
        fetch_input(str(args.year), str(args.day))

    sys.exit(0)
