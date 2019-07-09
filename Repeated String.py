#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the repeatedString function below.
def repeatedString(s, n):
    r=n%len(s)
    q=n//len(s)
    count=0
    if 'a' not in s:
        return 0
    c=dict(Counter(s))
    for i in range(r):
        if s[i]=='a':
            count+=1
    return c['a']*q+count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
