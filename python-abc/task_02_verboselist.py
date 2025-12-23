#!/usr/bin/env python3
class VerboseList(list):
    """VerboseList class"""
    def append(self, value):
        super().append(value)
        print(f"Added [{value}] to the list")

    def extend(self, iterable):
        count = len(iterable)
        super().extend(iterable)
        print(f"Extending the wlist with [{count}] items.")

    def remove(self, value):
        super().remove(value)
        print(f"Removed [{value}] from the list.")

    def pop(self, index=None):
        if index is None:
            value = super().pop()
            print(f"Popped [{value}] from the list.")
        else:
            value = super().pop(index)
            print(f"Popped [{value}] from the list.")
        return value
