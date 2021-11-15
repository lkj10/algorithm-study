import sys

sys.stdin = open("input.txt", "r")

dice = [ ['-', 0, '-'],
        [0,   0,    0],
        ['-', 0, '-'],
        ['-', 0, '-']
        ]

N, M, dice_y, dice_x, K = map(int, input().split())

Map = [list(map(int, input().split())) for _ in range(N)]

def left(): # 2
    temp = dice[1][0]
    dice[1][0] = dice[1][1]
    dice[1][1] = dice[1][2]
    dice[1][2] = dice[3][1]
    dice[3][1] = temp

def right(): # 1
    temp = dice[1][2]
    dice[1][2] = dice[1][1]
    dice[1][1] = dice[1][0]
    dice[1][0] = dice[3][1]
    dice[3][1] = temp

def down(): # 4
    temp = dice[3][1]
    dice[3][1] = dice[2][1]
    dice[2][1] = dice[1][1]
    dice[1][1] = dice[0][1]
    dice[0][1] = temp    

def up(): # 3
    temp = dice[0][1]
    dice[0][1] = dice[1][1]
    dice[1][1] = dice[2][1]
    dice[2][1] = dice[3][1]
    dice[3][1] = temp

cmd = list(map(int, input().split()))

for i in cmd:
    if i == 1: # 동쪽
        xx = dice_x + 1
        yy = dice_y
        if 0 <= yy < N and 0 <= xx < M :
            right()
            if Map[yy][xx] == 0: # 바닥이 0 인경우
                Map[yy][xx] = dice[3][1] # 바닥에 복사

            else : # 바닥이 0이 아닌 경우
                dice[3][1] = Map[yy][xx]
                Map[yy][xx] = 0
            dice_y = yy
            dice_x = xx
            print(dice[1][1])

    if i == 2: # 서쪽
        xx = dice_x - 1
        yy = dice_y
        if 0 <= yy < N and 0 <= xx < M :
            left()
            if Map[yy][xx] == 0: # 바닥이 0 인경우
                Map[yy][xx] = dice[3][1] # 바닥에 복사

            else : # 바닥이 0이 아닌 경우
                dice[3][1] = Map[yy][xx]
                Map[yy][xx] = 0
            dice_y = yy
            dice_x = xx
            print(dice[1][1])

    if i == 3: # 북쪽
        xx = dice_x 
        yy = dice_y - 1
        if 0 <= yy < N and 0 <= xx < M :
            up()
            if Map[yy][xx] == 0: # 바닥이 0 인경우
                Map[yy][xx] = dice[3][1] # 바닥에 복사

            else : # 바닥이 0이 아닌 경우
                dice[3][1] = Map[yy][xx]
                Map[yy][xx] = 0
            dice_y = yy
            dice_x = xx
            print(dice[1][1])
        
    if i == 4: # 남쪽
        xx = dice_x 
        yy = dice_y + 1
        if 0 <= yy < N and 0 <= xx < M :
            down()
            if Map[yy][xx] == 0: # 바닥이 0 인경우
                Map[yy][xx] = dice[3][1] # 바닥에 복사

            else : # 바닥이 0이 아닌 경우
                dice[3][1] = Map[yy][xx]
                Map[yy][xx] = 0
            dice_y = yy
            dice_x = xx
            print(dice[1][1])
