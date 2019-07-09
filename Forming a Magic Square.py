#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    pos=[]
    sum2=[]
    pos.append([[8,3,4],[1,5,9],[6,7,2]])
    pos.append([[6,7,2],[1,5,9],[8,3,4]])
    pos.append([[4,3,8],[9,5,1],[2,7,6]])
    pos.append([[2,7,6],[9,5,1],[4,3,8]])
    pos.append([[8,1,6],[3,5,7],[4,9,2]])
    pos.append([[4,9,2],[3,5,7],[8,1,6]])
    pos.append([[6,1,8],[7,5,3],[2,9,4]])
    pos.append([[2,9,4],[7,5,3],[6,1,8]])
    for k in range(8):
        sum1=0
        for i in range(3):
            for j in range(3):
                sum1+=abs(pos[k][i][j]-s[i][j])
        sum2.append(sum1)
    return min(sum2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
