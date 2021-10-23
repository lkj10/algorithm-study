import sys
import copy
from collections import deque

sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
dir = [[[1],[2],[3],[4]], [[1,3], [2,4]], [[1,2], [2,3], [3,4], [4,1]], [[1,2,3], [2,3,4], [3,4,1], [4,1,2]], [[1,2,3,4]]]
List = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
dq = deque()

def wall(list):
    temp = copy.deepcopy(List)
    for list_1 in list:
        dir_list = list_1[2]
        for i in dir_list:
            y = list_1[0]
            x = list_1[1]
            while(1):
                y = y + dy[i-1]
                x = x + dx[i-1]
                if y >= N or y < 0 or x >= M or x < 0 or temp[y][x] == 6:
                    break
                if temp[y][x] != 0 or temp[y][x] == -1:
                    continue
                temp[y][x] = -1
    cnt = 0
    for y in range(N):
        for x in range(M):
            if temp[y][x] == 0:
                cnt += 1
    return cnt

temp_list = []
MAX = 21e8
def dfs(pre, level, target):
    global MAX
    if level == target:
        MAX = min(MAX, wall(temp_list))
        return

    for i in range(pre, len(dq)):
        y, x, dir_list = dq[i][0], dq[i][1], dir[dq[i][2]-1]
        if visit[i] == 0:
            visit[i] = 1
            for j in dir_list:
                temp_list.append([y, x, j])
                dfs(i, level + 1, target)
                temp_list.pop()
            visit[i] = 0

cnt = 0
for y in range(N):
    for x in range(M):
        if List[y][x] != 0 and List[y][x] != 6: # 빈 공간도 아니고 벽(6)도 아니면
            dq.append([y, x, List[y][x]])
            cnt += 1

visit = [0] * cnt
dfs(0, 0, cnt)

print(MAX)

