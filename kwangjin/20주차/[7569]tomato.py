import sys
from collections import deque
sys.stdin = open("input.txt", "r")

List = []
M, N, H = map(int , input().split())
for _ in range(N*H):
    List.append(list(map(int, input().split())))


dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, -N, N]

dq = deque()

def bfs():
    while(dq):
        z, y, x = dq.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < M and z*N <= yy < z*N + N and List[yy][xx] == 0:
                List[yy][xx] = List[y][x] + 1
                dq.append((z, yy, xx))
        for i in range(4, 6):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < M and 0 <= yy < H*N and List[yy][xx] == 0:
                List[yy][xx] = List[y][x] + 1
                dq.append((z+dy[i]/N, yy, xx))
    

def check():
    MAX = 0
    for y in range(N*H):
        for x in range(M):
            if List[y][x] == 0:
                print(-1)
                return
            MAX = max(List[y][x], MAX)
    print(MAX-1)

for z in range(H):
    for y in range(z*N, z*N + N):
        for x in range(M):
            if List[y][x] > 0:
                dq.append((z, y, x))

bfs()
check()