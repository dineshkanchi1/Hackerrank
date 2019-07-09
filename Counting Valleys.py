#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    count=0
    valley=0
    for i in s:
        flag=0
        if count==0:
            flag=1
        if(i=='U'):
            count=count+1
        else:
            count=count-1
        if(count<0 and flag==1):
            valley=valley+1
    return valley
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
