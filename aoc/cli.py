import os
import importlib.resources as resources


def generate_template(year: str, day: str) -> None:
    """
    Creates a python file in the directory for the given year and names it
    after the given day. Expects a directory named after the year to be present
    in the CWD. If not found, creates the directory.
    :param year: The year.
    :param day: The day.
    :return: None
    """
    if not os.path.isdir(year):
        print(f'Couldn\'t find directory named {year} in cwd ({os.getcwd()}), creating new directory named {year}/')
        os.makedirs(year)

    if len(day) == 1:
        day = '0' + day

    file_path = f'{year}\\{day}.py'
    if os.path.exists(file_path):
        overwrite = input(f'{file_path} already exists. Do you want to overwrite its contents (y/n)? - ').strip()[0].lower()
        while overwrite not in ['y', 'n']:
            overwrite = input(f'Enter "y" for yes and "n" for no. Got {overwrite} - ').strip()[0].lower()
        if overwrite != 'y':
            return
        else:
            print(f'Overwriting {file_path}')

    template = resources.path('aoc.templates', 'day_template.txt')
    with template as f:
        lines = open(f).readlines()

    input_path = f'{year}\\input-{day}.txt'
    for line in lines:
        if '{{ input_path }}' in line:
            line.replace('{{ input_path }}', input_path)

    with open(file_path, 'w') as file:
        for line in lines:
            file.write(line)
