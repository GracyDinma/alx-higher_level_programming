#!/usr/bin/python3
"""Module 1-rectangle
Define a Rectangle class.
"""


class Rectangle:
    """Defines the width and height of the Rectangle class."""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle instance.

        Args
        width = width of the rectangle
        height = height of the rectangle.
        """
        self.width = 0
        self.height = 0

        @property
        def width(self):
            """Retrives the width of the Rectangle object"""
            return self.__width

        @width.setter
        def width(self, value):
            """Sets the width of a Rectangle object

            Args:
                value: value of the width must be a positive integer.
            """
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

            @property
            def height(self):
                """Retrieves the height of a Rectangle object."""
                return self.__height

            @height.setter
            def height(self, value):
                """Sets the height of a Rectangle instance

                Args:
                value: value of the width, must be a positive integer
                """
                if not  isinstance(value, int):
                    raise TypeError("height must be an integer")
                if value < 0:
                    raise ValueError("height must be >= 0")
                self.__height = value
