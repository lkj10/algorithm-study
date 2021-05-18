import sys
sys.stdin = open("input.txt", "r")

T = int(sys.stdin.readline())
SUM = 1
i = 0
while 1:
    SUM += 6*i
    i += 1
    if SUM >= T:
        print(i)
        break
