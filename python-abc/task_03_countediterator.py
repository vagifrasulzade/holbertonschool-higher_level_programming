#!/usr/bin/env python3
class CountedIterator:
    """Iterator that counts the number of iterations."""

    def __init__(self, iterable):
        self._iterable = iter(iterable)
        self._count = 0

    def __next__(self):
        item = next(self._iterable)
        self._count += 1
        return item

    def get_count(self):
        return self._count
