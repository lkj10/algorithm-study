import sys
sys.stdin = open("input.txt", 'r')
N, M = map(int, sys.stdin.readline().split())
dy = [0] *(M + 1)
for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    for j in range(M, B-1, -1):
        dy[j] = max(dy[j], dy[j-B] + A)

print(dy[M])
