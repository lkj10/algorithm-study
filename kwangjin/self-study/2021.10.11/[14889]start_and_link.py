import sys
sys.setrecursionlimit(100001)
T = int(sys.stdin.readline())
List = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]
visit = [0 for _ in range(T)]
res = 2100000000

def dfs(idx, level):
    global res
    if level == T//2:
        SUM_start, SUM_link = 0, 0
        for y in range(T):
            for x in range(y+1, T):
                if visit[y] and visit[x] :
                    SUM_start += List[y][x] + List[x][y]
                elif not visit[y] and not visit[x]:
                    SUM_link += List[y][x] + List[x][y]
        res = min(res, abs(SUM_start - SUM_link))

    for i in range(idx, T-1):
        if visit[i]:
            continue
        visit[i] = 1
        dfs(i+1, level+1)
        visit[i] = 0

dfs(0, 0)
print(res)