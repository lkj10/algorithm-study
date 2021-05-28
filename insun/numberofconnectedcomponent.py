# 연결 요소의 개수
# 문제: 방향 없는 그래프가 주어졌을 때, 연결 요소의 개수를 구하는 프로그램을 작성하시오
# 깊이 우선 탐색, 인접 리스트 사용
# 재귀를 사용하여 모든 노드 탐색을 완료한 뒤 cnt 1씩 증가
#  input()으로 받으면 시간 초과로 sys로 받아야 함.
import sys

sys.setrecursionlimit(1000000)


def dfs(v):
    visited[v] = True
    for j in node[v]:
        if not visited[j]:
            dfs(j)


n, m = map(int, input().split())
node = [[] for i in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    node[u].append(v)
    node[v].append(u)

cnt = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)
