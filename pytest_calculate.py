import unittest

from calculate import CustomCalculator

def test_calculate_pytest():
    assert CustomCalculator.calculate(2, 2) == 4

class TestCustomCalculatorUnittest(unittest.TestCase):
    def test_calculate_unittest(self):
        self.assertEqual(CustomCalculator.calculate(3, 3), 6)
