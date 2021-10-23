import sys
sys.stdin = open("input.txt", "r")

N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

y, x = N//2, N//2 # 중심 좌표

left = [(-2, 0, 0.02), (2, 0, 0.02), (-1, -1, 0.1), (-1, 0, 0.07), (-1, 1, 0.01), (1, -1, 0.1), (1, 0, 0.07), (1, 1, 0.01), (0, -2, 0.05), (0, -1, 0)] 
right = [(x, -y, z) for x, y, z in left] 
down = [(-y, x, z) for x, y, z in left] 
up = [(-x, y, z) for x, y, z in down]

def foo(dir, direction):
    global y, x, cnt, ans
    for _ in range(cnt): # 왼쪽
        y += dy[dir]
        x += dx[dir]
        if y < 0 or x < 0 : return -1
        if Map[y][x] > 0:
            res = 0
            for dyy, dxx, r in direction:
                ny = y + dyy
                nx = x + dxx
                if r == 0: 
                    sand = Map[y][x] - res
                else:
                    sand = int(Map[y][x] * r)
                if 0 <= nx < N and 0 <= ny < N:
                    Map[ny][nx] += sand
                else:
                    ans += sand
                res += sand
cnt = 1
ans = 0

while 1:
    if foo(0, left) == -1 : break
    if foo(3, down) == -1 : break
    cnt += 1
    if foo(2, right) == -1 : break
    if foo(1, up) == -1 : break
    cnt += 1


print(ans)


