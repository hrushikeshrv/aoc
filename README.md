# AOC
My attempts at Advent of Code, along with a small helper library to streamline daily AoC tasks.  
[Advent of Code 2020](https://adventofcode.com/2020)  
[Advent of Code 2021](https://adventofcode.com/2021)  
[Advent of Code 2022](https://adventofcode.com/2022)  
[Advent of Code 2023](https://adventofcode.com/2023)  
[Advent of Code 2024](https://adventofcode.com/2024)

You can find documentation for this library at [hrus.in/aoc/](https://hrus.in/aoc/)

## Compliance with AoC Guidelines
The helper and utility functions included in this library follow the automation guidelines given by the [Advent of Code Wiki](https://www.reddit.com/r/adventofcode/wiki/faqs/automation).

Specifically:
- No automated requests are made, only user initiated.
- Inputs are only fetched if they don't exist locally, and user confirmation is asked if overwriting local input.
- All local solutions are cached before submitting, and if the user tries to submit a solution that is already stored and known to be incorrect, no request is made and user is informed of incorrect solution.
- All requests contain a `User-Agent` header returned by `aoc.utils.get_request_headers` with my contact information, since I maintain this tool.

## Installing This Library
I've mainly written this package just for myself, and so it follows my preferred directory structure and solution template for solving AoC problems. But you're welcome to use this package if you want to!

You can find documentation for the API at [hrus.in/aoc/](https://hrus.in/aoc/)

Since the `aoc` name is already taken on PyPI, to use this library, you will have to install it from this source code in a virtual environment.

1. Get the source code by cloning this repository.
2. Create a directory for your Advent of Code solutions. All of your AoC solutions (even for future years) will be stored in this directory.
3. Create a virtual environment by running `python -m venv venv`, or use your preferred virtual environment.
4. Activate your virtual environment.
5. Install this code by running the following from the project's root directory -
```bash
pip install -e .
```

You can now use the helper functions in this library! You can find documentation for the API in `docs/`.
