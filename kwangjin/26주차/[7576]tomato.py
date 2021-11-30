import sys
from collections import deque


sys.stdin = open("input.txt", "r")

M, N = map(int, input().split())

List = [list(map(int, input().split())) for _ in range(N)]

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]
dq = deque()

check = 0
check2 = 0

def ans_check():
    global check, check2
    ans = 0 # 조건 따지는거.
    if check == 0 and check2 == 0: # 아무것도 없을 때
        return -1
    if check == 0: # 모두가 익어있는 상태
        return 0
    for y in range(N):
        for x in range(M):
            if List[y][x] == 0:
                return -1
            ans = max(List[y][x], ans)
    return ans-1

def bfs():
    global check
    while dq:
        y, x = dq.popleft()
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            if 0 <= yy < N and 0 <= xx < M and List[yy][xx] != -1 and List[yy][xx] == 0:
                List[yy][xx] = List[y][x] + 1
                check += 1 # 토마토가 있고, 주변에 감염시킬 무언가.
                dq.append([yy, xx])



for y in range(N):
    for x in range(M):
        if List[y][x] == 1:
            check2 = 1
            dq.append([y, x]) #토마토가 있다는 조건

bfs()
print(ans_check())