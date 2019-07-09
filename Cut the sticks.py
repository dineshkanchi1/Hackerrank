#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    l=[]
    n=len(arr)
    while(n!=0):
        x=min(arr)
        print(x)
        if x!=0:
            l.append(n)
            for i in range(len(arr)):
                arr[i]=arr[i]-x
        else:
            arr.remove(x)
            n-=1
    return l

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
