import sys
import copy
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())

ans = 21e8
def dfs(cnt, pre, level):
    global ans
    if level == M:
        temp = copy.deepcopy(List)
        for i in range(cnt):
            if visit[i] == 0:
                temp[ch_list[i][0]][ch_list[i][1]] = 0
        SUM = 0
        for y in range(N):
            for x in range(N):
                if temp[y][x] == 1 :
                    MIN = 21e8
                    for i in range(len(ch_list)):
                        if visit[i] == 1:
                            yy = ch_list[i][0]
                            xx = ch_list[i][1]
                            MIN = min(MIN, abs(yy-y) + abs(xx - x))
                    SUM += MIN
        ans = min(ans, SUM)
        return
    for i in range(pre, cnt):
        if visit[i] == 0:
            visit[i] = 1
            dfs(cnt, i, level + 1)
            visit[i] = 0
        
List = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
ch_list = []
for y in range(N):
    for x in range(N):
        if List[y][x] == 2:
            ch_list.append([y, x])
            cnt += 1
 
visit = [0]*cnt
dfs(cnt, 0, 0)
print(ans)