#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    n=len(c)
    jump=0
    i=0
    while(i<n-2):
        if c[i+2]==1:
            i+=1
        else:
            i+=2
        jump+=1
    if i+2==n:
        jump+=1
    return jump


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
