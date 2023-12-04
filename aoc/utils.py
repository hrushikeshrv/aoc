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
