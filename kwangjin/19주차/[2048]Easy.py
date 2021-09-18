import sys
sys.stdin = open("input.txt", "r")

# 왼 오 아 위 함수만들고 dfs
# 최댓값 저장

MAX = 0
List = []
N = int(input())

def dfs(cnt):
    global MAX, List
    if cnt == 5:
        print(List)
        for y in range(N):
            for x in range(N):
                MAX = max(List[y][x], MAX)

        return 
    for i in range(4):
        left()
        dfs(cnt+1)
        right()
        dfs(cnt+1)
        down()
        dfs(cnt+1)
        up()
        dfs(cnt+1)        


def left():
    for y in range(N):
        for x in range(N-1):
            if List[y][x] == 0:
                List[y][x], List[y][x+1] = List[y][x+1], List[y][x]

    for y in range(N):
        for x in range(N-1):
            if List[y][x] == List[y][x+1]:
                List[y][x] = List[y][x]*2
                List[y][x+1] = 0
                
def right():
    for y in range(N):
        for x in range(N-1, 0, -1):
            if List[y][x] == 0:
                List[y][x], List[y][x-1] = List[y][x-1], List[y][x]

    for y in range(N):
        for x in range(N-1, 0, -1):
            if List[y][x] == List[y][x-1]:
                List[y][x] = List[y][x]*2
                List[y][x-1] = 0

def down():
    for x in range(N):
        for y in range(N-1, 0, -1):
            if List[y][x] == 0:
                List[y][x], List[y-1][x] = List[y-1][x], List[y][x]

    for x in range(N):
        for y in range(N-1, 0, -1):
            if List[y][x] == List[y-1][x]:
                List[y][x] = List[y][x]*2
                List[y-1][x] = 0

def up():
    for x in range(N):
        for y in range(N-1):
            if List[y][x] == 0:
                List[y][x], List[y+1][x] = List[y+1][x], List[y][x]

    for x in range(N):
        for y in range(N-1):
            if List[y][x] == List[y+1][x]:
                List[y][x] = List[y][x]*2
                List[y+1][x] = 0


for _ in range(N):
    List.append(list(map(int, input().split())))

dfs(0)

print(MAX)


