n = int(input())
cad = ""
for i in range(n):
    cad = cad + str(i+1)

for i in range(len(cad)-1):
    print(cad[i:])
cad = cad[::-1]
for i in range(len(cad)):
    print(cad[:i+1])