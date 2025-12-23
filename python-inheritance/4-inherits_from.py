#!/usr/bin/python3
"""Module that defines inherits_from function"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited
    from a_class (directly or indirectly), but not a_class itself.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
