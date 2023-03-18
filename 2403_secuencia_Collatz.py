def S(x,c):
    if(x==1 or x==-1):
        print(c)
    else:
        c+=1
        if(x%2==0):
            S(x//2,c)
        else:
            S(3*x+1,c)

T = int(input())
for i in range(T):
    try:
        a = int(input())
        if(a==1):
            print(3)
        elif(a==-1):
            print(2)
        else:
            S(a,0)
    except RecursionError :
        print(-1)