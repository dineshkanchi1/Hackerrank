#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    l=Counter(sorted(s)).most_common(3)
    for i in l:
        print(i[0],i[1])
