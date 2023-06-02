line = input().split()
modulo = int(line[1])
pre, pos = int(line[2]), int(line[3])
n = int(line[0])
val = 0
if n == 1:
    print(pre)
if n == 2:
    print(pos)
if n > 2:
    for i in range(3, n+1):
        val = pre + pos
        pre = pos
        pos = val

    print(val%modulo)