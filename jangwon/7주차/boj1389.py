import sys
sys.stdin = open("input.txt", "r")

INF = int(1e9)
N, M = map(int, input().split())
graph = [[INF] * (N + 1) for _ in range(N + 1)]
result = [0 for _ in range(N + 1)]
answer = 0
# 본인은 0으로 
for i in range(1, N + 1):
  for j in range(1, N + 1):
    if i == j:
      graph[i][j] = 0

# 그래프 구성
for _ in range(M):
  u, v = map(int, input().split())
  graph[u][v] = 1
  graph[v][u] = 1

# 플로이드 워셜 알고리즘
for k in range(1, N + 1):
  for i in range(1, N + 1):
    for j in range(1, N + 1):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, N + 1):
  sum = 0
  for g in graph[i]:
    if g != INF:
      sum += g
  result[i] = sum

min_num = min(result[1:])
for idx, v in enumerate(result[1:]):
  if min_num == v:
    print(idx + 1)
    break