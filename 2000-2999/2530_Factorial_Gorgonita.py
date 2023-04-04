n = int(input())
while n <= 0:
    n = int(input())

factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1

print(factorial)


