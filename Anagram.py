#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the anagram function below.
def anagram(s):
    n=len(s)
    if n%2!=0:
        return -1
    else:
        a=s[:n//2]
        b=s[n//2:]
        c=0

        for i in a:
            if i in b:
                b=b.replace(i,'',1)
                continue
            c+=1
        return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
