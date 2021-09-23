import sys
from collections import deque
import copy
sys.stdin = open("input.txt", "r")

N = int(input())
List = []
for _ in range(N):
    List.append(list(map(int, input().split())))
ans = 0

def move_and_merge(dir):
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
    
        for y in range(N):
            idx = deque()
            for x in range(N):
                if List[y][x] == 0:
                    idx.append(x)
                elif idx:
                    List[y][idx.popleft()] = List[y][x]
                    List[y][x] = 0
                    idx.append(x)

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

        for x in range(N):
            idx = deque()
            for y in range(N):
                if List[y][x] == 0:
                    idx.append(y)
                elif idx:
                    List[idx.popleft()][x] = List[y][x]
                    List[y][x] = 0
                    idx.append(y)

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

        for y in range(N):
            idx = deque()
            for x in range(N-1, -1, -1):
                if List[y][x] == 0:
                    idx.append(x)
                elif idx:
                    List[y][idx.popleft()] = List[y][x]
                    List[y][x] = 0
                    idx.append(x)


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
                    
        for x in range(N):
            idx = deque()
            for y in range(N-1, -1, -1):
                if List[y][x] == 0:
                    idx.append(y)
                elif idx:
                    List[idx.popleft()][x] = List[y][x]
                    List[y][x] = 0
                    idx.append(y)

def dfs(level):
    global ans, List
    if level == 5:
        for i in range(N):
            ans = max(ans, max(List[i]))
        return
    tmp = copy.deepcopy(List)
    for i in range(4):
        move_and_merge(i)
        dfs(level+1)
        List = copy.deepcopy(tmp)


dfs(0)
print(ans)