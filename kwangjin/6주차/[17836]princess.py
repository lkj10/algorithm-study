from collections import deque
import sys
sys.stdin = open("input.txt", "r")
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M, T = map(int, input().split())

# List = list()
# visit = list()

# MIN = 214700000
# for _ in range(N):
#     List.append(list(map(int, input().split())))
#     visit.append([0]*M)

# visit[0][0] = 1


# def DFS(L, x, y):
#     global MIN

#     if L > T:
#         return
#     if x == M - 1 and y == N - 1:
#         MIN = min(L, MIN)
#         return
#     else:
#         for i in range(4):
#             dx = [-1, 0, 1, 0]
#             dy = [0, 1, 0, -1]
#             xx = x + dx[i]
#             yy = y + dy[i]
#             if M > xx >= 0 and N > yy >= 0 and visit[xx][yy] == 0 and List[xx][yy] != 1:
#                 visit[xx][yy] = 1
#                 if List[xx][yy] == 2:
#                     MIN = N + M - yy - xx - 1 + L
#                 DFS(L+1, xx, yy)
#                 visit[yy][xx] = 0


# DFS(0, 0, 0)

# if MIN > T:
#     print('Fail')
# else:
#     print(MIN)

# DFS로 푸니까 계속 답이 안나와서 BFS로 문제 풀어봄.


List = list()
dis = list()

for _ in range(N):
    List.append(list(map(int, input().split())))
    dis.append([0]*M)

Q = deque()
Q.append((0, 0))
sword_x, sword_y, sword_Time = 0, 0, 21470000000
get_sword = 0

if List[0][0] == 2:
    get_sword = 1
    sword_x, sword_y = 0, 0

while Q:
    tmp = Q.popleft()
    for i in range(4):
        x = tmp[0]+dx[i]
        y = tmp[1]+dy[i]
        if 0 <= x < N and 0 <= y < M and List[x][y] != 1:
            if List[x][y] == 2:
                get_sword = 1
                sword_x, sword_y = x, y
            List[x][y] = 1
            dis[x][y] = dis[tmp[0]][tmp[1]]+1
            Q.append((x, y))

if get_sword == 1:
    sword_Time = N + M + dis[sword_x][sword_y] - 2 - sword_x - sword_y

if dis[N-1][M-1] == 0 and sword_Time > T:
    print('Fail')
elif dis[N-1][M-1] == 0 and sword_Time <= T:
    print(sword_Time)
else:
    print(min(dis[N-1][M-1], sword_Time))


# 16퍼에서 계속 틀림.
