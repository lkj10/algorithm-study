import sys
sys.stdin = open("input.txt", "r")

N = int(input())
List = []
color = [0, 0]

def bfs(start_x, end_x, start_y, end_y, size):
    global cnt
    temp = List[start_y][start_x]
    for y in range(start_y, end_y):
        for x in range(start_x, end_x):
            if List[y][x] != temp:
                bfs(start_x, end_x - size//2 , start_y, end_y - size//2, size//2)
                bfs(start_x + size//2, end_x, start_y, end_y - size//2, size//2)
                bfs(start_x, end_x - size//2, start_y + size//2, end_y, size//2)
                bfs(start_x + size//2, end_x, start_y + size//2, end_y, size//2)
                return
    else:
        color[temp] += 1

for _ in range(N):
    List.append(list(map(int, input().split())))
bfs(0, N, 0, N, N)
for i in color:
    print(i)
