#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)
        """
        new_list = self.copy()
        new_list.sort()
        print(new_list)
