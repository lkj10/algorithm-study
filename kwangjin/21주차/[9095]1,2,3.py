import sys

sys.stdin = open("input.txt", "r")


List = [0, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274]
T = int(input())

for _ in range(T):
    n = int(input())
    print(List[n])


