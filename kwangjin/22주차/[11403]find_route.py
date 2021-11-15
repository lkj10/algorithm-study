import sys

sys.stdin = open("input.txt", "r")

N = int(input())
List = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for y in range(N):
        for x in range(N):
            if List[y][k] == 1 and List[k][x] == 1: # k노드를 거쳤을 때 1이면
                List[y][x] = 1 # 그건 연결되어있다.

for y in range(N):
    for x in range(N):
        print(List[y][x], end=' ')
    print()
