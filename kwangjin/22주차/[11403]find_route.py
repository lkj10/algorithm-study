import sys


sys.stdin = open("input.txt", "r")

N = int(input())
List = [list(map(int, input().split())) for _ in range(N)]

for i in List:
    print(i)