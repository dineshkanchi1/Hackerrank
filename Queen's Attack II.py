import sys
n,k=map(int,input().split(' '))
r,c=map(int,input().split(' '))
l=[]
for _ in range(k):
    r1,c1 = map(int,input().split(' '))
    l.append((r1,c1))
obstacle=set(l)
Delta=[(0,1),(1,1),(1,0),(0,-1),(-1,-1),(-1,0),(1,-1),(-1,1)]
Count=0
for shift in Delta:
    Pos = (r,c)
    while Pos[0]+shift[0]>=1 and Pos[0]+shift[0]<=n and Pos[1]+shift[1]>=1 and Pos[1]+shift[1]<=n:
        Pos=(Pos[0]+shift[0],Pos[1]+shift[1])
        if Pos in obstacle:
            break
        Count += 1
print(Count)
