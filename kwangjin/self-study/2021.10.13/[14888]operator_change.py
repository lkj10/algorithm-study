import sys
sys.stdin = open("input.txt", "r")
N = int(input())
List = list(map(int, input().split()))
op = list(map(int, input().split()))
visit = []
MAX = -21e8
MIN = 21e8
def dfs(level):
    global MAX, MIN
    if level == N-1:
        SUM = List[0]
        for i in range(N-1):
            if visit[i] == 0:
                SUM += List[i+1]
            if visit[i] == 1:
                SUM -= List[i+1]
            if visit[i] == 2:
                SUM *= List[i+1]
            if visit[i] == 3:
                if SUM < 0:
                    SUM *= -1
                    SUM /= List[i+1]
                    SUM *= -1
                    SUM = int(SUM)
                else : 
                    SUM /= List[i+1]
                    SUM = int(SUM)
        MAX = max(MAX, SUM)
        MIN = min(MIN, SUM)
        return

    for i in range(4):
        if op[i] > 0:
            op[i] -= 1
            visit.append(i)
            dfs(level+1)
            op[i] += 1
            visit.pop()

dfs(0)
print(MAX)
print(MIN)