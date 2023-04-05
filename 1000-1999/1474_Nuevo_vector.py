n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
vector3 = []
for i in range(n):
    operacion = input()
    if operacion =="+":
        vector3.append(a[i]+b[i])
    elif operacion =="*":
        vector3.append(a[i]*b[i])
    elif operacion == ">":
        vector3.append(max(a[i],b[i]))
    else:
        vector3.append(min(a[i],b[i]))
for i in range(0,n):
    print(vector3[i])