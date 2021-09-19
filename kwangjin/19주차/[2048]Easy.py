import sys
from collections import deque
sys.stdin = open("input.txt", "r")

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))


def move_and_merge(List, dir):
    if dir == 0: # left
        for y in range(N):
            idx = deque()
            for x in range(N):
                if List[y][x] == 0:
                    idx.append(x)
                elif idx:
                    List[y][idx.popleft()] = List[y][x]
                    List[y][x] = 0
                    idx.append(x)

        for y in range(N):
            for x in range(N-1):
                if List[y][x] == List[y][x+1]:
                    List[y][x] = List[y][x]*2
                    List[y][x+1] = 0

    if dir == 1: # up
        for x in range(N):
            idx = deque()
            for y in range(N):
                if List[y][x] == 0:
                    idx.append(y)
                elif idx:
                    List[idx.popleft()][x] = List[y][x]
                    List[y][x] = 0
                    idx.append(y)

        for x in range(N):
            for y in range(N-1):
                if List[y][x] == List[y+1][x]:
                    List[y][x] = List[y][x]*2
                    List[y+1][x] = 0

    if dir == 2: # right
        for y in range(N):
            idx = deque()
            for x in range(N-1, -1, -1):
                if List[y][x] == 0:
                    idx.append(x)
                elif idx:
                    List[y][idx.popleft()] = List[y][x]
                    List[y][x] = 0
                    idx.append(x)

        for y in range(N):
            for x in range(N-1, 0, -1):
                if List[y][x] == List[y][x-1]:
                    List[y][x] = List[y][x]*2
                    List[y][x-1] = 0

    if dir == 3: # down
        for x in range(N):
            idx = deque()
            for y in range(N-1, -1, -1):
                if List[y][x] == 0:
                    idx.append(y)
                elif idx:
                    List[idx.popleft()][x] = List[y][x]
                    List[y][x] = 0
                    idx.append(y)

        for x in range(N):
            for y in range(N-1, 0, -1):
                if List[y][x] == List[y-1][x]:
                    List[y][x] = List[y][x]*2
                    List[y-1][x] = 0


def dfs(List, level):
    if level == 5:
        print(List)
        return

    for i in range(2):
        move_and_merge(List, i)
        dfs(List, level+1)


dfs(arr, 0)