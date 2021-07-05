import sys
from collections import deque
sys.stdin = open("input.txt", "r")


def DFS(L):
    print(L, end=' ')
    visit[L] = 1
    for i in List:
        if i[0] == L and visit[i[1]] == 0:
            DFS(i[1])


def BFS(V):
    dq.append(V)
    visit[V] = 0
    while dq:
        temp = dq.popleft()
        print(temp, end=' ')
        for i in List:
            if i[0] == temp and visit[i[1]] == 1:
                dq.append(i[1])
                visit[i[1]] = 0


N, M, V = map(int, input().split())
List = list()
visit = [0]*(N+1)
dq = deque()
for _ in range(M):
    A, B = map(int, input().split())
    List.append((A, B))
    List.append((B, A))

List.sort(key=lambda x: (x[1], x[0]))

DFS(V)
print()
BFS(V)
