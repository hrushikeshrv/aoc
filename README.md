# AOC
My attempts at Advent of Code, along with a small helper package to streamline AoC tasks.  
[Advent of Code 2020](https://adventofcode.com/2020)  
[Advent of Code 2021](https://adventofcode.com/2021)  
[Advent of Code 2022](https://adventofcode.com/2022)  
[Advent of Code 2023](https://adventofcode.com/2023)

## Compliance with AoC Guidelines
The helper and utility functions included in this package follow the guidelines given by the [Advent of Code Wiki](https://www.reddit.com/r/adventofcode/wiki/faqs/automation).

Specifically:
- No automated requests are made, only user initiated.
- Inputs are only fetched if they don't exist locally, and user confirmation is asked if overwriting local input.
- All local solutions are cached before submitting, and if the user tries to submit a solution that is already stored and known to be incorrect, no request is made and user is informed of incorrect solution.
- All requests contain a `User-Agent` header returned by `aoc.utils.get_request_headers` with my contact information, since I maintain this tool.