import sys

sys.stdin = open("input.txt", "r")

M, N = map(int, sys.stdin.readline().split())
List = list(map(int, sys.stdin.readline().split()))

pre = [0]*(M+1)
pre[0] = 0
pre[1] = List[0]

for i in range(2, M+1):
    pre[i] = pre[i-1] + List[i-1] # M

for _ in range(N): #N
    i, j = map(int, sys.stdin.readline().split())
    print(pre[j]-pre[i-1])

