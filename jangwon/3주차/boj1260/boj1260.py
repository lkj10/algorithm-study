import sys
import collections
sys.stdin = open("input.txt", "r")
n, m, s = map(int, input().split())

# 인접리스트로 그래프 만들기 
graph = collections.defaultdict(list)
for _ in range(m):
  start, end = map(int,input().split())
  graph[start].append(end)
  graph[end].append(start)

def dfs(start, visited=[]):
  visited.append(start)
  for w in graph[start]:
    if w not in visited:
      visited = dfs(w, visited)
  
  return visited

def bfs(start):
  visited = [start]
  queue = collections.deque()
  queue.append(start)

  while queue:
    v = queue.popleft()
    for w in graph[v]:
      if w not in visited:
        queue.append(w)
        visited.append(w)

  return visited 


print(*dfs(s))
print(*bfs(s))