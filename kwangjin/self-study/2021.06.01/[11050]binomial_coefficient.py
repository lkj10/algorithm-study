import sys
sys.stdin = open("input.txt", "r")

M, N = map(int, input().split())

SUM = 1

for i in range(1, N+1):
    SUM *= (M-i+1) / i

print(int(SUM))