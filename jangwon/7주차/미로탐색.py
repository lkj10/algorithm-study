import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input())))

# 상하좌우
dx = [0, 0 , -1 ,1]
dy = [1, -1 , 0 ,0]

def bfs(x, y):
  q = deque()
  q.append((x, y))

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y

      if nx >= 0 and ny >= 0 and nx < n and ny < m and graph[nx][ny] == 1:
      # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
        if graph[nx][ny] == 1:
          graph[nx][ny] = graph[x][y] + 1
          q.append((nx, ny))

        
  return graph[n - 1][m - 1]

print(bfs(0, 0))