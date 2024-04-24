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

    def update(self, *args, **kwargs):
        """Update attributes of an instance.

        Args:
            -id attribute
            -size attribute
            -x attribute
            -y attribute
        """

        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                size.x = args[2]
            if len(args) > 3:
                size.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Update dictionary representation of square"""

        my_dict = {'id': self.id, 'size': self.size,
                   'x': self.x, 'y': self.y}
        return my_dict
