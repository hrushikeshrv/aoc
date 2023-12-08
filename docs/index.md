# AOC
My attempts at Advent of Code, along with a small helper library to streamline my daily AoC tasks.  

## Installation
I've mainly written this package just for myself, and so it follows my preferred directory structure and solution template for solving AoC problems. But you're welcome to use this package if you want to!

Since the `aoc` name is already taken on PyPI, to use this library, you will have to install it from this source code in a virtual environment.

1. Get the source code by cloning this repository.
2. Create a directory for your Advent of Code solutions. All of your AoC solutions (even for future years) will be stored in this directory.
3. Create a virtual environment by running `python -m venv venv`, or use your preferred virtual environment.
4. Activate your virtual environment.
5. Install this code by running the following from the project's root directory -
```bash
pip install -e .
```

You can now use the helper functions in this library! You can find documentation for the API below.

## Usage
This library provides the following features -

1. Generate a solution file for a particular AoC day using the Python template present in `aoc.templates`
2. Fetch your puzzle input for a specific AoC day

Make sure you activate the virtual environment in which you have installed this library before using these features.

To get a quick overview of the features offered by the CLI, run

```bash
aoc -h
```

### Generating A Solution File
To generate a solution file for a particular day, use the `-c` or `--create` flag.

```bash
aoc -c [year] [day]
```

If either the `year` or `day` arguments are not given, they default to the current year and the current day. So you can generate a solution file for today by running 

```bash
aoc -c
```

To generate a solution file for a particular year and day that is not today, run

```bash
aoc -c 2022 12
```

The above command will generate a solution file for day 12, 2022.

All solution files are stored in a directory named after the year. The library looks for a directory named after the year you passed in, in the working directory from which you run the command. So if you run all commands from the project root, all solution files will be stored in `./{year}/`.

The solution files are named `day{day}.py`, for example, `day01.py` to `day25.py`.

### Fetching Your Puzzle Input
To fetch your input for a particular day, use the `-f` or `--fetch` flag.

```bash
aoc -f [year] [day]
```

If either the `year` or `day` arguments are not given, they default to the current year and the current day. So you can fetch today's puzzle input by running 

```bash
aoc -f
```

To fetch your puzzle input for a particular year and day that is not today, run

```bash
aoc -f 2022 12
```

This above command will fetch your puzzle input for day 12, 2022.

Note: In order to fetch your puzzle input, you need to provide your session token for adventofcode.com  
See [Getting Your Session Token](#getting-your-session-token)

### Getting Your Session Token
Follow these steps to get your session token -

1. Log into [Advent of Code](https://adventofcode.com).
2. Open your browser's Developer Tools.
3. Navigate to the Application tab.
4. Look for the Cookies menu, and under the Cookies menu, look for https://adventofcode.com
5. Copy the value of the cookie named "session"
6. Run the following command
```bash
aoc --set-token <your-session-token>
```
Replace `<your-session-token>` with the cookie you copied. Your session token will be saved and used for all requests made to adventofcode.com. In case your session token expires, the CLI will notify you and prompt you to enter a new session token.