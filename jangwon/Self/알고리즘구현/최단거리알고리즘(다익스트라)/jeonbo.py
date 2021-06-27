# 파이썬 이것이 코딩 테스트다 -> 전보
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력 받기
n, m, start = map(int, input().split())

graph = [[] for _ in range(n + 1)]

distance = [INF] * (n + 1)

for _ in range(m):
  u, v, w = map(int, input().split())
  graph[u].append((v, w))

def djikstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue
    
    for i in graph[now]:
      cost  = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

djikstra(start)

cnt = 0
max_distance = 0

for d in distance:
  if d != INF:
    cnt += 1
    max_distance = max(max_distance, d)

print(cnt - 1, max_distance)








