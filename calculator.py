#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Description     : This includes functions for a calculator
# Author          : Barry Sheppard - Student Number 10387786
# Date            : 20181110
# Version         : 0.1
# Notes           : For CA5. Updated from CA1
# Python version  : 3.6.5
###############################################################################

# The math module is used for mathematical functions and math.pi
import math
# numbers is used to get the number.Real object type for comparison
import numbers
# For reduce function
from functools import reduce


def CheckIsNumber(input):
    return isinstance(input, numbers.Real)


def Add(first, second=0):
    ''' This returns the multiplication of two or more numbers '''
    if type(first) == list:
        return reduce(lambda x, y: x+y, first)
    if (isinstance(first, numbers.Real) and isinstance(second, numbers.Real)):
        return first + second
    raise TypeError('The Add function only takes numbers')


def CosineDegrees(first):
    ''' This returns the cosine of one or more numbers in degrees'''
    if type(first) == list:
        return list(map(lambda x: math.cos(x*(math.pi / 180)), first))
    if isinstance(first, numbers.Real):
        return math.cos(first*(math.pi / 180))
    raise TypeError('The Cosine function only takes numbers')


def Cube(first):
    ''' This returns the first number cubed '''
    if type(first) == list:
        return list(map(lambda x: x ** 3, first))
    if isinstance(first, numbers.Real):
        return first ** 3
    raise TypeError('The Cube function only takes numbers')


def Divide(first, second=1):
    ''' Returns the first number divided one or more numbers sequentially '''
    if type(first) == list:
        return reduce(lambda x, y: x/y, first)
    if (isinstance(first, numbers.Real) and isinstance(first, numbers.Real)):
        if second == 0:
            raise ZeroDivisionError('Cannot divide by Zero')
        return first / second
    raise TypeError('The Divide function only takes numbers')


def Exponent(first, second=1):
    ''' Returns first number to the power one or more numbers sequentially '''
    if type(first) == list:
        return reduce(lambda x, y: x ** y, first)
    if (isinstance(first, numbers.Real) and isinstance(first, numbers.Real)):
        return first ** second
    raise TypeError('The Exponent function only takes numbers')


def Multiply(first, second=1):
    ''' This returns the multiplication of one or more numbers '''
    if type(first) == list:
        return reduce(lambda x, y: x * y, first)
    if (isinstance(first, numbers.Real) and isinstance(first, numbers.Real)):
        return first * second
    raise TypeError('The Multiply function only takes numbers')


def SineDegrees(first):
    ''' This returns the sine of the input number in degrees'''
    if type(first) == list:
        return list(map(lambda x: math.sin(x*(math.pi / 180)), first))
    if isinstance(first, numbers.Real):
        return math.sin(first*(math.pi / 180))
    raise TypeError('The SineDegrees function only takes numbers')


def SquareRoot(first):
    ''' This the square root of one or more numbers '''
    if type(first) == list:
        return list(map(lambda x: math.sqrt(x), first))
    if isinstance(first, numbers.Real):
        return math.sqrt(first)
    raise TypeError('The SquareRoot function only takes numbers')


def Square(first):
    ''' This returns square of one or more numbers '''
    if type(first) == list:
        return list(map(lambda x: x ** 2, first))
    if isinstance(first, numbers.Real):
        return first ** 2
    raise TypeError('The Square function only takes numbers')


def Subtract(first, second=1):
    ''' This returns the first number less one ore more numbers '''
    if type(first) == list:
        return reduce(lambda x, y: x - y, first)
    if isinstance(first, numbers.Real):
        return first - second
    raise TypeError('The Subtract function only takes numbers')


def TangentDegrees(first):
    ''' This returns the tangent of the input number in degrees

    This will raise a ZeroDivisionError for angles of 90 or 270
    '''
    # Tan of 90 or 270 degrees will result in an error
    # This also applies to angles larger than 360 + 90 etc, so we need to use
    # the modulus for the remainder.
    # As the conversion to radians isn't exact due to the computer not
    # having an exact number for pi, the check needs to be in place to avoid
    # the code returning the tan for a value very close to 90 or 270 degrees
    # Without this check, the math.tan function will return a result that is
    # very high as a number very close to 90 or 270 degress will have a result.
    if type(first) == list:
        return list(map(lambda x: math.tan(x*(math.pi / 180)), first))
    if isinstance(first, numbers.Real):
        if first % 360 in [90, 270]:
            raise ZeroDivisionError('Tan of 90 or 270 are undefined')
        return math.tan(first*(math.pi / 180))
    raise TypeError('The TangentDegrees function only takes numbers')
