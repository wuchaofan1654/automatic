# -*- coding: utf-8 -*-
"""
Create by sandy at 16:24 24/04/2022
Description: ToDo
"""


class Colored:
    HEADER = '\033[95m'
    BLUE = '\033[94m'  # blue
    SUCCESS = '\033[92m'  # green
    WARNING = '\033[93m'  # yellow
    DANGER = '\033[91m'  # red
    BLACK = '\033[0m'  # black
    BOLD = '\033[1m'  # black+bold
    UNDERLINE = '\033[4m'  # black+underline

    def __new__(cls, color=SUCCESS, underline=False, bold=False, content=None):

        if color.lower() in ['success', 'ok']:
            content = f"{cls.SUCCESS}{content}{cls.BLACK}"

        elif color.lower() in ['warning', 'warn']:
            content = f"{cls.WARNING}{content}{cls.BLACK}"

        elif color.lower() in ['danger', 'error']:
            content = f"{cls.DANGER}{content}{cls.BLACK}"

        content = underline and f"{cls.UNDERLINE}{content}{cls.BLACK}" or content
        content = bold and f"{cls.BOLD}{content}{cls.BLACK}" or content

        return content

if __name__ == '__main__':
    def test():
        print(Colored(content='it is sandy!', color='SUCCESS', bold=True, underline=False))
        print("is is ")

    test()
