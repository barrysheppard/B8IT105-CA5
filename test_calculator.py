#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Description     : This will run unit tests on the calculator.py script
# Author          : Barry Sheppard - Student Number 10387786
# Date            : 20180923
# Version         : 0.4
# Notes           : For CA5. No change from CA1
# Python version  : 3.6.5
###############################################################################

# This file is used to test the calculator.py file.
# This is saved under test_calculator.py

# The unittest module has options that will help us test our functions
import unittest
# We import the functions we want to test from the file calc
from calculator import (Add, CosineDegrees, Cube, Divide, Exponent, Multiply,
                        SineDegrees, Square, SquareRoot, Subtract,
                        TangentDegrees)
# To test arrays of numbers which are almost equal we need numpy
import numpy as np


class CalculatorTest(unittest.TestCase):
    # the (unittest.TestCase) has this class extend the TestCase class
    # contained within the unittest module

    # The test functions must start with test or they will not run.

    def testAdd(self):
        # Test for some basic numbers
        self.assertEqual(4, Add(2, 2))
        self.assertEqual(2, Add(0, 2))
        # Adding negative numbers should result in negatives
        self.assertEqual(-5, Add(-1, -4))
        # Should work for floats as well as ints
        self.assertEqual(3.12312, Add(1.12312, 2))
        # If both input are not numbers we should get a TypeError
        self.assertRaises(TypeError, Add, "text", 0)
        # New addition of lists
        self.assertEqual(6, Add([1, 2, 3]))
        # Currently lists of non-numbers cause problems

    def testCosineDegrees(self):
        # Test for some basic numbers, due to rounding of pi we use AlmostEqual
        self.assertAlmostEqual(0, CosineDegrees(90))
        self.assertAlmostEqual(0.70710678118, CosineDegrees(45))
        # Negative values are valid
        self.assertAlmostEqual(0, CosineDegrees(-90))
        # As are degrees greater than 360
        self.assertAlmostEqual(0, CosineDegrees(450))
        self.assertAlmostEqual(CosineDegrees(45), CosineDegrees(405))
        # If input is not a number we should get a TypeError
        self.assertRaises(TypeError, CosineDegrees, "text")
        # New addition of lists
        np.testing.assert_almost_equal([0, 0], CosineDegrees([90, 90]))
        # Currently lists of non-numbers cause problems

    def testCube(self):
        # Test for some basic numbers
        self.assertEqual(8, Cube(2))
        # Test with negatives
        self.assertEqual(-8, Cube(-2))
        # If input is not a number we should get a TypeError
        self.assertRaises(TypeError, Cube, "text")
        # self.assertRaises(TypeError, Cube, [1, 2, 3])
        self.assertEqual([1, 8, 27], Cube([1, 2, 3]))
        # Currently lists of non-numbers cause problems

    def testDivide(self):
        # Test for some basic numbers
        self.assertEqual(1, Divide(2, 2))
        self.assertEqual(2.5, Divide(5, 2))
        # Confirm an error will be raised if the second number is zero
        self.assertRaises(ZeroDivisionError, Divide, 5, 0)
        # If input is not a number we should get a TypeError
        self.assertRaises(TypeError, Divide, "text")
        # self.assertRaises(TypeError, Divide, [1, 2, 3])
        self.assertEqual(1, Divide([9, 3, 3]))
        # Currently lists of non-numbers cause problems

    def testExpontent(self):
        # Test for some basic numbers
        self.assertEqual(4, Exponent(2, 2))
        self.assertEqual(1, Exponent(5, 0))
        self.assertEqual(5, Exponent(5, 1))
        # An negative exponent divides rather than multiplies
        self.assertEqual(5, Exponent(0.2, -1))
        # An expontent of 0 results in a result of 1
        self.assertEqual(1, Exponent(5, 0))
        self.assertEqual(1, Exponent(100, 0))
        # If input is not a number we should get a TypeError
        self.assertRaises(TypeError, Exponent, "text")
        # self.assertRaises(TypeError, Add, [1, 2, 3], [1, 2, 3])
        self.assertEqual(16, Exponent([2, 2, 2]))
        # Currently lists of non-numbers cause problems

    def testMultiply(self):
        # Test for some basic numbers
        self.assertEqual(4, Multiply(2, 2))
        self.assertEqual(0, Multiply(5, 0))
        self.assertEqual(5, Multiply(5, 1))
        # If there is one negative number the result should be negative
        self.assertEqual(-5, Multiply(-5, 1))
        # If there are two negative numbers the result should be positive
        self.assertEqual(5, Multiply(-5, -1))
        # If input is not a number we should get a TypeError
        self.assertRaises(TypeError, Multiply, "text")
        # self.assertRaises(TypeError, Multiply, [1, 2, 3])
        self.assertEqual(6, Multiply([1, 2, 3]))
        # Currently lists of non-numbers cause problems

    def testSineDegrees(self):
        # Test for some basic numbers, due to rounding of pi we use AlmostEqual
        self.assertAlmostEqual(1, SineDegrees(90))
        # If input is not a number we should get a TypeError
        self.assertRaises(TypeError, SineDegrees, "text")
        # self.assertRaises(TypeError, SineDegrees, [1, 2, 3])
        # New addition of lists
        np.testing.assert_almost_equal([1, 1], SineDegrees([90, 90]))
        # Currently lists of non-numbers cause problems

    def testSquare(self):
        # Test for some basic numbers
        self.assertEqual(4, Square(2))
        # If input is not a number we should get a TypeError
        self.assertRaises(TypeError, Square, "text")
        # self.assertRaises(TypeError, Add, [1, 2, 3])
        self.assertEqual([4, 9], Square([2, 3]))
        # Currently lists of non-numbers cause problems

    def testSquareRoot(self):
        # Test for some basic numbers
        self.assertEqual(2, SquareRoot(4))
        # If input is not a number we should get a TypeError
        self.assertRaises(TypeError, SquareRoot, "text")
        # self.assertRaises(TypeError, Add, [1, 2, 3])
        self.assertEqual([2, 3], SquareRoot([4, 9]))
        # Currently lists of non-numbers cause problems

    def testSubtract(self):
        # Test for some basic numbers
        self.assertEqual(0, Subtract(2, 2))
        self.assertEqual(5, Subtract(5, 0))
        self.assertEqual(4, Subtract(5, 1))
        # If the second number is larger than the first the result is negative
        self.assertEqual(-1, Subtract(5, 6))
        # If input is not a number we should get a TypeError
        self.assertRaises(TypeError, Subtract, "text")
        # self.assertRaises(TypeError, Subtract, [1, 2, 3])
        self.assertEqual(5, Subtract([10, 2, 3]))
        # Currently lists of non-numbers cause problems

    def testTangentDegrees(self):
        # Test for some basic numbers, due to rounding of pi we use AlmostEqual
        self.assertAlmostEqual(0, TangentDegrees(180))
        # Confirm an error will be raised if the second number is zero
        self.assertRaises(ZeroDivisionError, TangentDegrees, 90)
        # If input is not a number we should get a TypeError
        self.assertRaises(TypeError, TangentDegrees, "text")
        # self.assertRaises(TypeError, TangentDegrees, [1, 2, 3])
        # New addition of lists
        np.testing.assert_almost_equal([0, 0], TangentDegrees([180, 180]))
        # Currently lists of non-numbers cause problems

# This piece of code looks for any function that extends unittest and
# runs it. So in this case it will run all the functions within the code
unittest.main()
