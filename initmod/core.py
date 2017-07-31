# -*- coding: utf-8 -*-
"""Add Docstring here"""


def helloworld():
    """initmod test function"""
    print('hello world')  # pylint: disable=superfluous-parens


def main():
    """Add Dockstring here"""
    print("Inside __main__.main()")  # pylint: disable=superfluous-parens


if __name__ == "__main__":
    # execute only if run as a script
    main()
