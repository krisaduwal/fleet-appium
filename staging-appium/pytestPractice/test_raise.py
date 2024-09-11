import pytest
import math


# def func(x):
#     if x <= 0:
#         raise ValueError("x needs to be larger than zero")
#         # print(ValueError)
#
# pytest.raises(ValueError, func, x=-3)


def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

def testsquare():
   num = 7
   assert 7*7 == 40

def testequality():
   assert 10 == 11