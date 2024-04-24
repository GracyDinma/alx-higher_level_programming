#!/usr/bin/python3
"""Test case for Rectangle class"""

import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestRectangle(unittest.Testcase):
    """Test for rectangle class"""

    def test_pep8_conformance(self):
        """Test that the code conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Fount code style errors (and warning).")

        def test_rectangle_subclass(self):
            """Test whether Rectangle class inherit from Base class."""

            self.assertTrue(issubclass(Rectangle, Base))
