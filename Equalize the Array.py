#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the equalizeArray function below.
def equalizeArray(arr):
    l=dict(Counter(arr))
    print(l)
    l=list(l.values())
    print(l)
    max1=max(l)
    l.remove(max1)
    return sum(l)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
