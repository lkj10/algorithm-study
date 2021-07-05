import sys
from collections import deque
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())

List = list()
dq = deque()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
for _ in range(N):
    List.append(list(map(int, input())))

dq.append((0, 0))

while dq:
    x, y = dq.popleft()
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if M > xx >= 0 and N > yy >= 0 and List[yy][xx] == 1:
            List[yy][xx] = List[y][x] + 1
            dq.append((xx, yy))

print(List[N-1][M-1])
