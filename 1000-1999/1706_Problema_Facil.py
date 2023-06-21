import sys
if __name__ == "__main__":
    for line in sys.stdin:
        p = input()
        if(p.__contains__("1")):
            print("HARD")
        else:
            print("EASY")