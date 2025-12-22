#!/usr/bin/python3
"""This module contains the class MyList"""


class MyList(list):
    """A subclass of list"""

    def print_sorted(self):
        print(sorted(self))
