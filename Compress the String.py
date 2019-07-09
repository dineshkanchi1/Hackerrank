# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
s=list(input())

a=[]
b=[]
for i,j in groupby(s):
    a.append(list(j))
    b.append(i)

for i in range(len(b)):
    print("({}, {})".format(len(a[i]),b[i]),end=' ')
