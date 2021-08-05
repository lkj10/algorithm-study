import sys
sys.stdin = open("input.txt", 'r')
n, m = map(int(sys.stdin.readline()).split())
dy = [0] * (m+1)
for i in range(n):
    w, v = map(int, sys.stdin.readline().split())
    for j in range(w, m+1):
        dy[j] = max(dy[j], dy[j-w]+v)

print(dy)