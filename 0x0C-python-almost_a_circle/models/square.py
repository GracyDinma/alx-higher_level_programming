#!/usr/bin/python3
"""Module Square
Create a class Square that inherits from a rectangle.
"""

import models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class describing a square
    public attribute

    area()
    display
    update()
    to_dict()

    inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the class

        Args:
        size: size of square
        x: x of square
        y: y of square
        id: id of square.
        """

        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation

        """
        s = "[Square] ({}) {}/{} - {}".format(
                self.id, self.__x, self.__y, self.__width)

        return s

    @property
    def size(self):
        """Retrieves the size attribute."""

        return self.__width

    @size.setter
    def size(self, value):
        """Sets the size of the attribute"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value
