import sys
sys.stdin = open("input.txt", "r")

N, r, c = map(int, input().split())

List = [[0]*(2**N) for i in range(2**N)]
visit = [[0]*(2**N) for i in range(2**N)]

cnt = 0

for i in range(2**N):
    for j in range(2**N):
        if visit[i][j] == 0: 
            for k in range(4):
                List[i + k//2][j + k%2] = cnt + k
                visit[i + k//2][j + k%2] = 1
            else:
                cnt += 4
                
print(List[r][c])
    