"""
Sample tests
"""

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""   
    def test_add_numbers(self):
        """test adding numbers together"""
        res = calc.add(5, 4)
        self.assertEqual(res, 9)

    def test_substract_numbers(self):
        """Test subtract numbers."""
        res = calc.subtract(10, 15)
        self.assertEqual(res, 5)
