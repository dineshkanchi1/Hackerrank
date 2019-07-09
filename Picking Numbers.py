#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    c=0
    for i in a:
        if(i==5):
            c+=1

    print(c)
    a=sorted(a)
    b=dict()
    for i in a:
        b[i]=0
    for i in a:
        b[i]+=1

    if len(b)==1:
        return b[i]
    print(b)
    key=list(b.keys())
    values=list(b.values())
    sum1=[]
    for i in range(len(key)):
        for j in range(i+1,len(key)):
            if(abs(key[i]-key[j])==0 or abs(key[i]-key[j])==1):
                sum1.append(values[i]+values[j])
            else:
                break
    return max(max(b.values()),max(sum1))

    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
