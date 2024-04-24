#!/usr/bin/python3
"""Module 2
Defines a class Rectangle that inherits from Base.
"""
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
        
        super().__init_(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        """private instance attributes."""
    @property
    def width(self):
        """Retrieves the width attribute."""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width attribute."""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height attribute."""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height attribute."""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieves the x attribute."""

        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x attribute."""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieves the y attribute."""

        return self.__y

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

    def display(self):
        """Prints #."""

        for y in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            for x in range(0, self.__x):
                print(" ", end="")
            for j in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns a string representation of a Rectangle instance."""

        s = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
        return s

    def update(self, *args, **kwargs):
        """Updates attributes of an instance.

        Args:
            - id attribute
            - width attribute
            - height attribute
            - x attribute
            - y attribute
        """

        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns dictionary representation of Rectangle."""

        my_dict = {'id': self.id, 'width': self.__width,
                   'height': self.__height, 'x': self.__x, 'y': self.__y}
        return my_dict
