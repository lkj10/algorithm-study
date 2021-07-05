import sys
sys.stdin = open('input.txt', 'r')

INF = int(1e9)
N = int(input())
M = int(input())
graph = [[INF] * (N + 1) for _ in range(N + 1)]

# 그래프 구현
for _ in range(M):
  u, v, w = map(int, input().split())
  graph[u][v] = min(graph[u][v], w)

for i in range(1, N + 1):
  for j in range(1, N + 1):
    if i == j:
      graph[i][j] = 0
  
for k in range(1, N + 1):
  for i in range(1, N + 1):
    for j in range(1, N + 1):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for row in graph[1:]:
  for col in row[1:]:
    if(col == INF):
      print(0, end=" ")
    else :
      print(col, end=" ")
  print()