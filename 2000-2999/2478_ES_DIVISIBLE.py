# Problem : ES DIVISIBLE?
a,b= map(int, input().split())
if a%b == 0:
    print(str(a),"es divisible por",str(b))
elif b%a == 0:
    print(str(b),"es divisible por",str(a))
else:
    print("-1")
