import importlib.resources as resources

from pathlib import Path


def get_confirmation(message: str) -> bool:
    """
    Asks the user for confirmation before an action.
    :param message: The confirmation message to show
    :return: True if the user provides confirmation (enters "y" or similar), False otherwise
    """
    overwrite = input(message).strip()[0].lower()
    while overwrite not in ["y", "n"]:
        overwrite = (
            input(f'Enter "y" for yes and "n" for no. Got {overwrite} - ')
            .strip()[0]
            .lower()
        )
    return overwrite == "y"


def get_session_token() -> str:
    """
    Gets the stored session token from aoc.data.session_token.txt
    :return: The stored token, or an empty string if the token is not found
    """
    try:
        return resources.files("aoc.data").joinpath("session_token.txt").read_text()
    except FileNotFoundError:
        return ""


def set_session_token(token: str | None = None) -> str:
    """
    Prompts the user to enter their session token, stores it in the session file, and returns the same token
    :return: The token entered by the user
    """
    if token is None:
        token = input(
            "Enter your session token here, and it will be saved for future requests - "
        ).strip()
        while not token:
            print(f"Got an invalid token - {token}.")
            token = input(
                "Enter your session token here, and it will be saved for future requests - "
            ).strip()
    token_path = Path("./aoc/data/session_token.txt")
    with open(token_path, "w") as f:
        f.write(token)
    return token


def get_request_headers() -> dict[str, str]:
    """
    Returns the request headers that should be sent while talking to AoC servers
    :return: A dictionary of request headers
    """
    return {
        "User-Agent": "https://github.com/hrushikeshrv/aoc contact:hrushikeshrv@gmail.com"
    }
