from itertools import combinations
n=int(input())
l=list(input().split())
k=int(input())
pos=[]
pos=list(combinations(l,k))
m=len(pos)
count=0
for i in pos:
    if 'a' in i:
        count+=1
print(count/m)
