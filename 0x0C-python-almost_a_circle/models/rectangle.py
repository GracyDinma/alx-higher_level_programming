#!/usr/bin/python3
"""Module 2
Defines a class Rectangle that inherits from Base.
"""
import json
from models.base import Base


class Rectangle(Base):
    """Class describing a rectangle.
    Public instance methods:
        area()
        display()
        to_dictionary()
        update()
        that inherits from Base
        """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the attribute.

        Args:
            width: width of the instance
            height: height of the intance
            x: x of the instance
            y: y of the instance
            id: id of the instance
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init_(id)

        """private instance attributes."""
    @property
    def width(self):
        """Retrieves the width attribute."""

        return self.__width

    @property
    def height(self):
        """Retrieves the height attribute."""

        return self.__height

    @property
    def x(self):
        """Retrieves the x attribute."""

        return self.__x

    @property
    def y(self):
        """Retrieves the y attribute."""

        return self.__y

    @width.setter
    def width(self, value):
        """Sets the width attribute."""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height attribute."""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Sets the x attribute."""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Sets the y attribute."""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates the area of a Rectangle instance.

        Returns area
        """

        return self.__width * self.__height
