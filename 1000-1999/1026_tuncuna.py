from sys import stdin
from sys import stdout

test_cases = int(stdin.readline())

for case in range(test_cases):
    goal = int(stdin.readline())
    discriminant = ((8 * goal) + 1) ** (1/2)
    rows = (int(discriminant) - 1) // 2
    sum_rows = (rows * (rows + 1)) // 2
    
    if sum_rows == goal:
        stdout.write("Go On Bob " + str(rows) + "\n")
    else:
        stdout.write("Better Luck Next Time" + "\n")