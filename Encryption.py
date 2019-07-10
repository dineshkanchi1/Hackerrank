#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    cols = int(math.ceil(len(s)**0.5))
    x=''
    for i in range(cols):
        x+=''.join([s[x] for x in range(i, len(s), cols)])+" "
    return x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
