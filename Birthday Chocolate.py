#!/bin/python3
from itertools import combinations
import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    if(len(s)==1):
        return 1
    count=0
    l=list((s[i:i+m]) for i in range(0, len(s)))
    print(l)
    for i in l:
        if sum(i)%d==0:
            count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
