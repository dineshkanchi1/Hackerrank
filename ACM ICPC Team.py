n,m=list(map(int,input().split(' ')))
a=[]
for i in range(n):
    c=input()
    a.append(int(c,2))
b=[]
for i in range(n-1):
    for j in range(i+1,n):
        b.append(bin(a[i] | a[j]))
b=[x.count('1') for x in b]
b.sort()
print(b[-1])
print(b.count(b[-1]))
