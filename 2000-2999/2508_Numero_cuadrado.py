import math

def generate_perfect_squares(max_n):
    perfect_squares = []
    for i in range(1, int(math.sqrt(max_n))+1):
        perfect_squares.append(i*i)
    return perfect_squares

def count_perfect_squares_in_range(a, b, perfect_squares):
    count = 0
    for ps in perfect_squares:
        if a <= ps <= b:
            count += 1
    return count

T = int(input())
perfect_squares = generate_perfect_squares(10**9)
for i in range(T):
    a , b = map(int, input().split())
    perfect_squares_in_range = count_perfect_squares_in_range(a, b, perfect_squares)
    print(perfect_squares_in_range)
