n = int(input())
for i in range(n):
    x = int(input())
    numb = "1"
    for j in range(x-1):
        numb = numb + "0"
    print(int(str(numb),2))