import importlib.resources as resources
import requests


from aoc.utils import (
    confirm_overwrite,
    get_session_token,
    set_session_token,
    get_request_headers,
)

from pathlib import Path


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
            print(f"Overwriting {file_path}")

    template = (
        resources.files("aoc.templates").joinpath("python_day_template.txt").read_text()
    )
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
    dest = Path(f"./{year}/inputs")
    if not dest.exists():
        print(
            f"Couldn't find directory named {year}/inputs in cwd, creating new directory named ./{year}/inputs"
        )
        dest.mkdir()
    input_url = f"https://adventofcode.com/{year}/day/{day}/input"

    if len(day) == 1:
        day = "0" + day

    input_path = dest / f"input-{day}.txt"
    if input_path.exists():
        overwrite = confirm_overwrite(input_path)
        if not overwrite:
            return
        else:
            print(f"Overwriting {input_path}")

    session_token = get_session_token()
    if not session_token:
        print("Couldn't get your session token.")
        set_session_token()

    print(f"Fetching your input for {year} day {day}.")
    response = requests.get(
        input_url, cookies={"session": session_token}, headers=get_request_headers()
    )
    while not response.ok and response.status_code == 400:
        retry = input(
            "Couldn't fetch your input because your session token has expired or was incorrect. "
            "Do you want to enter your session token now and try again (y/n)? - "
        )
        while retry.strip().lower()[0] not in ["y", "n"]:
            retry = input(f'Enter "y" for yes and "n" for no, got {retry} - ')
        if retry != "y":
            return
        set_session_token()
        response = requests.get(
            input_url,
            cookies={"session": get_session_token()},
            headers=get_request_headers(),
        )

    with open(input_path, "w") as f:
        f.write(response.text)
    print(f"Input stored successfully in {input_path}")


def submit_answer(year: int, day: int, part: int, solution: str) -> bool:
    """
    Submits a solution for the given day and year
    :param year: The year
    :param day: The day
    :param part: The part
    :param solution: The solution
    :return: True if the solution is correct, False otherwise
    """
    # Parse aoc/data/solutions.json and check if this solution has been previously submitted for the current
    # Session token

    # If it has, return the same response as before

    # Otherwise, add this solution to the dictionary of submitted solutions and the response it received
