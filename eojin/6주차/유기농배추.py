import sys
from collections import deque

sys.stdin = open("input.txt")
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def protect(x, y, array, visited,n,m):
    visited[x][y]=True
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if  nx>=0 and nx< n and ny>=0 and ny < m and array[nx][ny]==1 and visited[nx][ny]==False:
                q.append((nx,ny))
                visited[nx][ny]=True

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    visited = [[False] * m for i in range(n)]
    array = [[0] * m for i in range(n)]
    count=0
    for _ in range(k):
        a, b = map(int, input().split())
        array[b][a] = 1

    for i in range(n):
        for j in range(m):
            if array[i][j] == 1 and visited[i][j] == False:
                protect(i,j,array,visited,n,m)
                count+=1

    print(count)