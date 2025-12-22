#!/usr/bin/python3
class MyList(list):
    def append(self, item):
        # only keep non-negative ints
        if item >= 0:
            super().append(item)

    def print_sorted(self):
        print(sorted(self))
