import sys
sys.stdin = open("input.txt", "r")

N = int(input())
List = []
cnt = 0
res = []
for _ in range(N):
    List.append(list(map(int, input())))

def bfs(y, x):
    global cnt
    List[y][x] = 0
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if( N > xx >= 0 and N > yy >= 0 and List[yy][xx] == 1):
            cnt += 1
            List[yy][xx] = 0
            bfs(yy, xx)


for y in range(N):
    for x in range(N):
        if List[y][x] == 1:
            cnt = 1
            bfs(y, x)
            res.append(cnt)

print(len(res))
for i in sorted(res):
    print(i)