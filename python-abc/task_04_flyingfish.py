#!/usr/bin/env python3

class Fish:
    """A class representing a fish."""

    def swim(self):
        print("The fish is swimming.")

    def habitat(self):
        print("The fish lives in water.")


class FlyingFish(Fish):
    """A class representing a flying fish, inheriting from Fish."""
    def swim(self):
        print("The flying fish is swimming!")

    def fly(self):
        print("The flying fish is soaring!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
