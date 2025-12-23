#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes"""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Circle class"""
    def __init__(self, radius):
        self.__radius = abs(radius)

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """Rectangle class"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())


if __name__ == "__main__":

    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=6)

    shape_info(circle)
    shape_info(rectangle)
