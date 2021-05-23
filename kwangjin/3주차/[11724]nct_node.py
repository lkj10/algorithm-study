import sys
sys.stdin=open("input.txt", "r")


def DFS(Node):
    global visit
    for i in Node:
        if i not in visit:
            visit.append(i)
            DFS(dic[i])
    
N, M = map(int, input().split())
dic = {}
visit = []
cnt = 0

for i in range(1, N+1):
    dic[i] = list()

for _ in range(M):
    u, v = map(int, input().split())
    dic[u].append(v)
    dic[v].append(u)

for i in dic:
    if i not in visit:
        DFS(dic[i])
        cnt += 1

print(cnt)