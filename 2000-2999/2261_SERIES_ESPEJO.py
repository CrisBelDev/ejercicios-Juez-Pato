n = int(input())
serie = []
for i in range(1, (n+1)):
    serie.append(i)
    serie.append(-i)

print(*serie[:n],"")
