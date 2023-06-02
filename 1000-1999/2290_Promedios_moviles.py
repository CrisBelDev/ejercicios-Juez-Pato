def primo(x):
    c=0
    for i in range(1,x+1):
        if(x%i==0):
            c+=1
    if(c==2):
        return True
    return False

t=int(input())
while(t>0):
    n=int(input())
    v=[]
    for _ in range(n):
        num=int(input())
        if(primo(num)):
            v.append(num)
    if(len(v)>=2):
        for i in range(1,len(v)):
            print((v[i-1]+v[i])//2)
    else:
        print("No existen promedios")
    t-=1

