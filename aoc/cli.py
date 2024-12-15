import argparse
import datetime
import pytz

import sys

from aoc.core import generate_template, fetch_input, run_solution
from aoc.utils import set_session_token


def main():
    parser = argparse.ArgumentParser(
        prog=__package__,
        description="A small helper package for streamlining Advent of Code tasks",
    )
    now = datetime.datetime.now(pytz.utc)
    est = pytz.timezone("US/Eastern")
    now = now.astimezone(est)

    parser.add_argument(
        "year",
        type=int,
        help="The AoC year you want to work with.",
        nargs="?",
        default=now.year,
    )
    parser.add_argument(
        "day",
        type=int,
        nargs="?",
        help="The AoC day you want to work with.",
        default=now.day,
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
        "-r",
        "--run",
        action="store_true",
        help="Run the solution file for a given year and day.",
    )
    parser.add_argument(
        "--set-token", help="Set your session token for communicating with AoC servers."
    )

    args = parser.parse_args()

    if args.year < 2015:
        print("The AoC year cannot be earlier than 2015!")
        sys.exit(1)

    if not 0 < args.day < 26:
        print("The AoC day must be between 1 and 25!")
        sys.exit(1)

    if args.set_token:
        set_session_token(args.set_token)

    if args.create:
        generate_template(str(args.year), str(args.day))

    if args.fetch:
        fetch_input(str(args.year), str(args.day))

    if args.run:
        run_solution(args.year, args.day)

    sys.exit(0)
