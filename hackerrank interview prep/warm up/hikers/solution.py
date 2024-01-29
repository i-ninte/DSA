#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
  #converting the paths to a list 
    path = list(path)
  # where altitude reprsents the height 
    altitude = 0
    map = []
    valleys = 0
    
    for step in path:
        if step == 'U':
            altitude += 1
            map.append(altitude)
            
        else:
            altitude -= 1 
            map.append(altitude)
    
    for n in range(0, len(map)):
        if map[n] == 0:
            if map[n-1] < 0:
                valleys += 1
               
    return valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
