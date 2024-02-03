#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    if s[-2:] == "AM":
        if s[:2] == "12":
            return "00" + s[2:-2]
        else:
            return s[:-2]
    elif s[-2:] == "PM":
        if s[:2] == "12":
            return s[:-2]  # If it's exactly 12:00:00 PM, return as is
        else:
            h = int(s[:2]) + 12
            return str(h) + s[2:-2]
    else:
        raise ValueError("Invalid time format")

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
 

