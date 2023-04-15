import sys

if __name__ == "__main__":
    for line in sys.stdin:
        i = input().split()
        X = []
        for x in i:
            X.append(int(x))
        X.sort()
        print(X[-1] - X[0])