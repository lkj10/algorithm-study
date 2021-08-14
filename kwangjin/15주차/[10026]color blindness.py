import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(100000)

def DFS(x, y):
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, -0]
    visit[x][y] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if N > xx >= 0 and N > yy >= 0 and visit[xx][yy] == 0:
            if List[x][y] == List[xx][yy]:
                visit[xx][yy] = 1
                DFS(xx, yy)
                if List[xx][yy] == 'G':
                    List[xx][yy] = 'R'


def search(N, visit):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0:
                DFS(i, j)
                if List[i][j] == 'G':
                    List[i][j] = 'R'
                cnt += 1
    return cnt


N = int(input())
List = []
visit = [[0]*N for _ in range(N)]

for i in range(N):
    List.append(list(input()))

print(search(N, visit), end=' ')
visit = [[0]*N for _ in range(N)]
print(search(N, visit))
