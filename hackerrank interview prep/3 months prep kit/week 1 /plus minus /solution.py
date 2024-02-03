#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive = 0
    negative = 0
    zero = 0
    for n in arr:
        if n < 0:
            negative += 1
        elif n > 0:
            positive += 1
        else:
            zero += 1
    print("{:.6f}".format(positive / len(arr)))
    print("{:.6f}".format(negative / len(arr)))
    print("{:.6f}".format(zero / len(arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

