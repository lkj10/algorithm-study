
import sys
sys.stdin = open("input.txt", "r")

sys.setrecursionlimit(10000)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def DFS(y, x):
    List[y][x] = 0
    for i in range(4):
        temp_y = y + dy[i]
        temp_x = x + dx[i]
        if 0 <= temp_y < N and 0 <= temp_x < M and List[temp_y][temp_x] == 1:
            DFS(temp_y, temp_x)

T = int(input())

for _ in range(T):
    cnt = 0
    M, N, K = map(int, input().split())
    List = [[0]*M for i in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        List[y][x] = 1

    for i in range(N):
        for j in range(M):
            if List[i][j] == 1:
                cnt += 1
                DFS(i, j)           

    print(cnt)