import math
N, M, A = map(int, input().split())
num_losas = math.ceil(N/A) * math.ceil(M/A)
print(num_losas)