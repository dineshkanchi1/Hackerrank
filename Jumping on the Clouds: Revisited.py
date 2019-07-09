#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    score=100
    index=(k)%len(c)
    while(score>0 and index!=0 and index!=len(c)-1):
        if c[index]==0:
            score-=1
        else:
            score=score-3
        index=(index+k)%len(c)
    if index==len(c)-1:
        if c[index]==0:
            score=score-1
        else:
            score=score-3
    if(c[0]==1):
        return score-3
    else:
        return score-1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
