def sd(x):
    return sum(int(d) for d in str(x))
def ordenarV(v):
    return sorted(v, key=lambda x: (sd(x), x))
n=int(input())
v=[int(x) for x in input().split()]
r=ordenarV(v)
for i in range(0,len(r)):
    if(len(r)-1==i):
        print(r[i])
    else:
        print(r[i],end=" ")