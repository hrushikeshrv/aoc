import argparse
import datetime
import importlib.resources as resources
import requests
import sys

from pathlib import Path

from aoc.utils import confirm_overwrite, get_session_token, set_session_token, get_request_headers


def generate_template(year: str, day: str) -> None:
    """
    Creates a python file in the directory for the given year and names it
    after the given day. Expects a directory named after the year to be present
    in the CWD. If not found, creates the directory.
    :param year: The year.
    :param day: The day.
    :return: None
    """
    year_dir = Path(f"./{year}")
    if not year_dir.exists():
        print(
            f"Couldn't find directory named {year} in cwd, creating new directory named ./{year}/"
        )
        year_dir.mkdir()

    if len(day) == 1:
        day = "0" + day

    file_path = year_dir / f"day{day}.py"
    if file_path.exists():
        overwrite = confirm_overwrite(file_path)
        if not overwrite:
            return
        else:
            print(f'Overwriting {file_path}')

    template = resources.files("aoc.templates").joinpath("day_template.txt").read_text()
    lines = template.split("\n")

    for i in range(len(lines)):
        line = lines[i]
        if "{{ input_path }}" in line:
            lines[i] = line.replace("{{ input_path }}", f"inputs/input-{day}.txt")

    with open(file_path, "w") as file:
        for line in lines:
            file.write(line + "\n")


def fetch_input(year: str, day: str) -> None:
    """
    Fetches input for the given year and day and stores it in "./{year}/inputs/input-{day}.txt"
    :param year: The AoC year you want to work with
    :param day: The AoC day you want to work with
    :return: None
    """
    dest = Path(f'./{year}/inputs')

    if len(day) == 1:
        day = "0" + day

    input_path = dest / f'input-{day}.txt'
    if input_path.exists():
        overwrite = confirm_overwrite(input_path)
        if not overwrite:
            return
        else:
            print(f'Overwriting {input_path}')

    session_token = get_session_token()
    if not session_token:
        print('Couldn\'t get your session token.')
        set_session_token()

    input_url = f'https://adventofcode.com/{year}/day/{day}/input'
    print(f'Fetching your input for {year} day {day}.')
    response = requests.get(input_url, cookies={'session': session_token}, headers=get_request_headers())
    print(response.text)


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

    args = parser.parse_args()

    if args.year < 2015:
        print("The AoC year cannot be earlier than 2015!")
        sys.exit(1)

    if args.create:
        generate_template(str(args.year), str(args.day))

    if args.fetch:
        fetch_input(str(args.year), str(args.day))

    sys.exit(0)
