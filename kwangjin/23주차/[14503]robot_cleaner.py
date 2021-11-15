import sys

sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())

robot_y, robot_x, robot_dir = map(int, input().split())

left = [(0, -1), (-1, 0), (0, 1), (1, 0)] # 각 방향에서 바라보는 왼쪽
back = [(1, 0), (0, -1), (-1, 0), (0, 1)] #한 칸 뒤로 이동

Map = [list(map(int, input().split())) for _ in range(N)]
visit = [[0]* M for _ in range(N)]


cnt = 0
visit[robot_y][robot_x] = 1

while 1:

    if visit[robot_y + left[robot_dir][0]][robot_x + left[robot_dir][1]] == 0 and Map[robot_y + left[robot_dir][0]][robot_x + left[robot_dir][1]] == 0:
        # 벽이 아니고, 청소를 하지 않았다면
        robot_y += left[robot_dir][0] # 그 방향으로 한칸 이동
        robot_x += left[robot_dir][1] # 그 방향으로 한칸 이동
        robot_dir = (robot_dir + 3) % 4 # 그 방향으로 회전한다.
        visit[robot_y][robot_x] = 1 # 거기를 방문했다(청소한다).
        cnt = 0
        continue # 다시 1번 부터 진행

    else :
        # 왼쪽 방향에 청소할 공간이 없다면
        robot_dir = (robot_dir + 3) % 4 # 그 방향으로 회전한다.
        cnt += 1

    if cnt == 4:
        robot_y += back[robot_dir][0]
        robot_x += back[robot_dir][1]
        if Map[robot_y][robot_x] == 1:
            break
        cnt = 0

ans = 0
for y in range(N):
    for x in range(M):
        ans += visit[y][x]

print(ans)






