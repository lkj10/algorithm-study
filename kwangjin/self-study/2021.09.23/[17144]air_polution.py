from collections import deque
import sys

sys.stdin = open("input.txt", "r")

R, C, T = map(int, input().split())

List = [list(map(int, input().split())) for _ in range(R)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

up_cleaner = [0, 0]
down_cleaner = [0, 0] 

def diffusion():
    temp = [[0]*C for _ in range(R)]
    temp[up_cleaner[0]][up_cleaner[1]] = -1
    temp[down_cleaner[0]][down_cleaner[1]] = -1
    while dq:
        y, x = dq.popleft()
        dir_cnt = 0
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            if 0 <= yy < R and 0 <= xx < C and List[yy][xx] != -1:
                dir_cnt += 1
                temp[yy][xx] += int(List[y][x]/5)
        temp[y][x] += List[y][x] - int((List[y][x]/5)) * dir_cnt
    for y in range(R):
        for x in range(C):
            List[y][x] = temp[y][x]
        
def cleaner():
    yy = up_cleaner[0]-1
    xx = up_cleaner[1]
    while(yy != up_cleaner[0] or xx != up_cleaner[1]):
        while(yy > 0): # 아랫 방향
            List[yy][xx] = List[yy-1][xx]
            yy -= 1
        while(xx < C-1): #왼쪽 방향
            List[yy][xx] = List[yy][xx+1]
            xx += 1
        while(yy < up_cleaner[0]): # 윗 방향
            List[yy][xx] = List[yy+1][xx]
            yy += 1
        while(xx > 0): # 오른쪽 방향
            List[yy][xx] = List[yy][xx-1]
            xx -= 1
        List[yy][xx+1] = 0
    
    yy = down_cleaner[0]+1
    xx = down_cleaner[1]
    while(yy != down_cleaner[0] or xx != down_cleaner[1]):
        while(yy < R-1): # 윗 방향
            List[yy][xx] = List[yy+1][xx]
            yy += 1
        while(xx < C-1): #왼쪽 방향
            List[yy][xx] = List[yy][xx+1]
            xx += 1
        while(yy > down_cleaner[0]): # 아랫 방향
            List[yy][xx] = List[yy-1][xx]
            yy -= 1
        while(xx > 0): # 오른쪽 방향
            List[yy][xx] = List[yy][xx-1]
            xx -= 1
        List[yy][xx+1] = 0




for _ in range(T):
    dq = deque()
    for y in range(R):
        for x in range(C):
            if List[y][x] > 0: # 미세먼지 좌표 저장
                dq.append((y, x))
            if List[y][x] == -1 and up_cleaner[0] == 0: # 공기청정기 윗 좌표 저장
                up_cleaner[0] = y
            elif List[y][x] == -1: # 공기청정기 아랫좌표 저장
                down_cleaner[0] = y
    diffusion()
    cleaner()

res = 0

for y in range(R):
    for x in range(C):
        if List[y][x] != -1:
            res += List[y][x]

print(res)
