import sys
sys.stdin = open("input.txt", "r")

N, M, V = map(int, input().split())
List = list()
for i in range(M):
    A, B = map(int, input().split())
    List.append((A, B))
List.sort(key=lambda x: (x[1], x[0]))

print(List)


def DFS():


def BFS():
