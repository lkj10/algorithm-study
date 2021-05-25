import sys
import collections
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
graph = collections.defaultdict(list)
visited = [False for _ in range(N + 1)]
count = 0

def dfs(v):
    visited[v] = True
    
    for w in graph[v]:
        if not visited[w]:
            dfs(w)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
for i in range(1, N + 1):
    if not visited[i]:
        count += 1
        dfs(i)

print(count)