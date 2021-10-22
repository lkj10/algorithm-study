import sys
import copy
sys.stdin = open("input.txt", "r")

N, M, K = map(int, input().split())
Map = [[0]*N for _ in range(N)]
box = [[[0, 0, []] for _ in range(N)] for _ in range(N)]  # visit, vect, dir

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    Map[r-1][c-1] = m
    box[r-1][c-1][0] += 1
    box[r-1][c-1][1] += s
    box[r-1][c-1][2].append(d)

for k in range(K):
    temp_Map = [[0]*N for _ in range(N)]
    temp_box = [[[0, 0, []] for _ in range(N)] for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if box[y][x][0] > 0:  # visit > 0 이상이면
                for i in box[y][x][2]:  # dir 리스트
                    yy = (y + dy[i]*int(box[y][x][1])) % N
                    xx = (x + dx[i]*int(box[y][x][1])) % N
                    temp_box[yy][xx][0] += 1
                    temp_Map[yy][xx] += Map[y][x]
                    temp_box[yy][xx][1] += box[y][x][1]
                    temp_box[yy][xx][2].append(i)

    for y in range(N):
        for x in range(N):
            if temp_box[y][x][0] > 1:
                temp_Map[y][x] = temp_Map[y][x]//5

                if temp_Map[y][x] == 0:  # 질량이 0이면
                    temp_box[y][x][0], temp_box[y][x][1], temp_box[y][x][2] = 0, 0, []
                    continue

                temp_box[y][x][1] = temp_box[y][x][1] // temp_box[y][x][0]
                odd, even = 0, 0
                for i in temp_box[y][x][2]:
                    if i % 2 == 0:
                        even = 1
                    elif i % 2 == 1:
                        odd = 1
                if even == 1 and odd == 1:  # 홀수, 짝수 둘 다 있으면
                    temp_box[y][x][2] = [1, 3, 5, 7]
                else:
                    temp_box[y][x][2] = [0, 2, 4, 6]

    Map = copy.deepcopy(temp_Map)
    box = copy.deepcopy(temp_box)


ans = 0

for y in range(N):
    for x in range(N):
        if Map[y][x] > 0:
            if box[y][x][0] > 1:
                ans += Map[y][x] * 4
            else:
                ans += Map[y][x]

print(ans)
