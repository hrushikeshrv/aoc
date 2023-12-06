import importlib.resources as resources

from pathlib import Path


def confirm_overwrite(path: Path | str) -> bool:
    """
    Asks the user whether they want to overwrite a given path and returns their answer.
    :param path: The path to overwrite
    :return: True if the path should be overwritten, False otherwise.
    """
    overwrite = (
        input(
            f"{path} already exists. Do you want to overwrite its contents (y/n)? - "
        )
        .strip()[0]
        .lower()
    )
    while overwrite not in ["y", "n"]:
        overwrite = (
            input(f'Enter "y" for yes and "n" for no. Got {overwrite} - ')
            .strip()[0]
            .lower()
        )
    return overwrite == 'y'


def get_session_token() -> str:
    """
    Gets the stored session token from aoc.data.session_token
    :return: The stored token, or an empty string if the token is not found
    """
    try:
        return resources.files('aoc.data').joinpath('session_token').read_text()
    except FileNotFoundError:
        return ''


def set_session_token() -> str:
    """
    Prompts the user to enter their session token, stores it in the session file, and returns the same token
    :return: The token entered by the user
    """
    token = input('Enter your session token here, and it will be saved for future requests - ')
    while not token:
        print(f'Got an invalid token - {token}.')
        token = input('Enter your session token here, and it will be saved for future requests - ')
    token_path = Path('./aoc/data/session_token')
    with open(token_path) as f:
        f.write(token)
    return token


def get_request_headers() -> dict[str, str]:
    """
    Returns the request headers that should be sent while talking to AoC servers
    :return: A dictionary of request headers
    """
    return {
        'User-Agent': f'https://github.com/hrushikeshrv/aoc contact:hrushikeshrv@gmail.com'
    }
