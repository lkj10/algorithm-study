import sys
import copy
from collections import deque
sys.stdin = open("input.txt", "r")

N, Q = map(int, input().split())

List = [list(map(int, input().split())) for _ in range(pow(2, N))]

cmd_List = list(map(int, input().split()))
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def firestorm(size):
    for y in range(0, pow(2, N), size):
        for x in range(0, pow(2, N), size):
            size_temp_List = [[0]*size for _ in range(size)]
            for yy in range(y, y + size):
                for xx in range(x, x + size):
                    size_temp_List[xx-x][size-yy+y-1] = List[yy][xx]

            for yy in range(y, y + size):
                for xx in range(x, x + size):
                    List[yy][xx] = size_temp_List[yy-y][xx-x]

    temp_List = copy.deepcopy(List)

    for y in range(pow(2, N)):
        for x in range(pow(2, N)):
            cnt = 0
            for i in range(4):
                yy = y + dy[i]
                xx = x + dx[i]
                if 0 <= yy < (pow(2, N)) and 0 <= xx < (pow(2, N)) and List[yy][xx] > 0:
                    cnt += 1
            if cnt < 3 and temp_List[y][x] > 0:
                temp_List[y][x] -= 1

    return temp_List


for i in cmd_List:
    temp_List = []
    List = copy.deepcopy(firestorm(pow(2, i)))

ans = 0
Max = 0

Group = [[0] * pow(2, N) for _ in range(pow(2, N))]
for y in range(pow(2, N)):
    for x in range(pow(2, N)):
        ans += List[y][x]
        if List[y][x] > 0 and Group[y][x] == 0:
            dq = deque([[y, x]])
            cnt = 1
            while dq:
                yy, xx = dq.popleft()
                Group[yy][xx] = 1
                for i in range(4):
                    yyy = yy + dy[i]
                    xxx = xx + dx[i]
                    if 0 <= yyy < (pow(2, N)) and 0 <= xxx < (pow(2, N)) and List[yyy][xxx] > 0 and Group[yyy][xxx] == 0:
                        dq.append([yyy, xxx])
                        Group[yyy][xxx] = 1
                        cnt += 1
            Max = max(cnt, Max)


print(ans)
print(Max)
