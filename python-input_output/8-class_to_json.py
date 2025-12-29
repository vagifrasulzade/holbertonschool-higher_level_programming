#!/usr/bin/python3
"""Module that returns the dictionary description for JSON serialization."""


def class_to_json(obj):
    """Returns a dictionary description with simple data structures."""
    return obj.__dict__.copy()
