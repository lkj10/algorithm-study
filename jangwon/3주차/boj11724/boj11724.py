# import sys
# sys.setrecursionlimit(10000)
# import collections
# n, m  = map(int, input().split())
# graph = collections.defaultdict(list)

# # 리스트 컴프리헨션 , 노드 방문 체크을 위한 리스트 생성, 노드의 개수 만큼
# checked = [False for _ in range(n + 1)]
# count = 0

# # 무방향 그래프 -> 간선을 양 쪽에 모두 할당
# for _ in range(m):
#   start, end = map(int, input().split())
#   graph[start].append(end)
#   graph[end].append(start)

# # DFS 방법으로 순회
# def dfs(start, checked):
#   checked = True
  
#   for w in graph[start]:
#     if not checked[w]:
#       dfs(w, checked)

# for i in range(1, len(checked)):
#   if checked[i] == False:
#     count += 1
#     dfs(i, checked)

# print(count)
# TypeError 'bool' object is not subscriptable -> if not checked[w]:

# 시간 초과 
import sys
import collections
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
# graph = collections.defaultdict(list)
graph = [[] for _ in range(N + 1)]
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