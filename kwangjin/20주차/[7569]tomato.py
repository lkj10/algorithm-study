import sys
sys.stdin = open("input.txt", "r")

List = []
M, N, H = map(int , input().split())
for _ in range(N*H):
    List.append(list(map(int, input().split())))


dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, -N, N]
day = 0

def foo():
    global day
    while(1):
        flag = 0
        res = [[0]*M for _ in range(N*H)]

        for y in range(N*H):
            for x in range(M):
                res[y][x] = List[y][x]

        for h in range(H):
            for y in range(h*N, h*N + N):
                for x in range(M):
                    if List[y][x] == 1:
                        for i in range(4):
                            yy = y + dy[i]
                            xx = x + dx[i]
                            if  h*N <= yy < h*N + N and 0 <= xx < M and List[yy][xx] == 0:
                                res[yy][xx] = 1
                                flag = 1

                        for i in range(4, 5):
                            yy = y + dy[i]
                            xx = x + dx[i]
                            if  0 <= yy < N*H and List[yy][xx] == 0:
                                res[yy][xx] = 1
                                flag = 1
        if flag == 0:
            for y in range(N*H):
                for x in range(M):
                    if List[y][x] == 0:
                        print(-1)
                        return
            print(day)
            return

        for y in range(N*H):
            for x in range(M):
                List[y][x] = res[y][x]

        day += 1

foo()
