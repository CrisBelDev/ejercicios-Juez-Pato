N = int(input())
x = 0
for i in range(N):
    sec = input()
    
    if sec.count("+")==2:
        x +=1
    else:
        x -=1
print(x)