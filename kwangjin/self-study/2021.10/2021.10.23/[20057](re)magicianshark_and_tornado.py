import sys
sys.stdin = open("input.txt", "r")

N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

left = [[-2, 0, 0.02], [-1, -1, 0.1],
        [-1, 0, 0.07], [-1, 1, 0.01],
        [0, -2, 0.05], [1, -1, 0.1], [1, 0, 0.07],
        [1, 1, 0.01], [2, 0, 0.02], [0, -1, 1]]
right = [[y, -x, r] for y, x, r in left]
up = [[x, y, r] for y, x, r in left]
down = [[-x, y, r] for y, x, r in left]

cn_y, cn_x = N//2, N//2
ans = 0


def tornado(cnt, dir, dir_list):
    global y, x, ans
    for _ in range(cnt):
        y += dy[dir]
        x += dx[dir]
        if y < 0 or x < 0:
            return -1
        res = 0
        target = Map[y][x]
        for dyy, dxx, r in dir_list:
            yyy = y + dyy
            xxx = x + dxx
            now = int(Map[y][x] * r)
            if r == 1:
                now = target - res
            if 0 <= yyy < N and 0 <= xxx < N:
                Map[yyy][xxx] += now
                target -= now
            else:
                res += now
        ans += res


dir_cnt = 1
y, x = cn_y, cn_x
while(1):
    if tornado(dir_cnt, 0, left) == -1:
        break
    if tornado(dir_cnt, 1, down) == -1:
        break
    dir_cnt += 1
    if tornado(dir_cnt, 2, right) == -1:
        break
    if tornado(dir_cnt, 3, up) == -1:
        break
    dir_cnt += 1

print(ans)
