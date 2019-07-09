#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    l=[i for i in range(len(q),0,-1)]
    c=0
    a=q[::-1]
    for i in range(0,len(q)):
        flag=0
        for j in range(i,len(q)):
            flag+=1
            if a[j]==l[i]:
                for k in range(j,i,-1):
                    a[k],a[k-1]=a[k-1],a[k]
                    c+=1
                break
            
        if flag>3:
            print("Too chaotic")
            return
    print(c)
                
            
    
                
                

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
