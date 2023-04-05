n = int(input())
for i in range(n):
    num= int(input())
    l = len(str(num))
    boolean = "SI!"
    for j in range(l-1):
        aux = num%10
        num = num/10
        if(int(num%10) <= aux):
            boolean = "NO!"
    print(boolean)