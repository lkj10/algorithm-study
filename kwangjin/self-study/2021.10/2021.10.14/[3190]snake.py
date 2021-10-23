from collections import deque
import sys
from collections import deque
sys.stdin = open("input.txt", "r")

N = int(input())
K = int(input())

def dir_change(dir, C):
    if C == 'D':
        dir = (dir + 1)%4
    else:
        dir = (dir - 1)%4
    return dir

List = [[0]*N for _ in range(N)]

dq = deque()

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


for _ in range(K):
    y, x = map(int, input().split())
    List[y-1][x-1] = 1

L = int(input())

dir_list = deque()
for _ in range(L):
    X, C = input().split()
    dir_list.append([int(X), C])

def straight():
    head_y = 0
    head_x = 0
    sec = 0
    dq.append([0, 0])
    List[0][0] = 2
    dir = 2
    while(1):
        X, C = dir_list.popleft()
        if not dir_list :
            dir_list.append([100, 'S'])
        while(1):
            sec += 1
            head_y += dy[dir]
            head_x += dx[dir]
            if 0 <= head_y < N and 0 <= head_x < N and List[head_y][head_x] != 2:
                if List[head_y][head_x] != 1:
                    temp_y, temp_x = dq.popleft()
                    List[temp_y][temp_x] = 0
                dq.append([head_y, head_x])
                List[head_y][head_x] = 2
            else:
                print(sec)
                return
            if sec == X :
                dir = dir_change(dir, C)
                break
            
straight()