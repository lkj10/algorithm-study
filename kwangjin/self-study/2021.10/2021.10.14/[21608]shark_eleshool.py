import sys
import heapq
sys.stdin = open("input.txt", "r")

N = int(input())
dic = {}
List = [[0]*N for _ in range(N)]

for i in range(N*N):
    temp = list(map(int, input().split()))
    dic[temp[0]] = [temp[1], temp[2], temp[3], temp[4]]

cnt = 0

dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

for key, val in dic.items():
    emp = []
    like = []
    for y in range(N):
        for x in range(N):
            if List[y][x] == 0:
                emp_cnt = 0
                like_cnt = 0
                for i in range(4):
                    yy = y + dy[i]
                    xx = x + dx[i]
                    if 0 <= yy < N and 0 <= xx < N and List[yy][xx] == 0:
                        emp_cnt += 1
                    if 0 <= yy < N and 0 <= xx < N and List[yy][xx] in val:
                        like_cnt += 1
                if like_cnt == 0 :
                    heapq.heappush(emp, (-emp_cnt, y, x))
                else:
                    heapq.heappush(like, (-like_cnt, -emp_cnt, y, x))
    if not like:
        temp = heapq.heappop(emp)
        List[temp[1]][temp[2]] = key
    else:
        temp = heapq.heappop(like)
        List[temp[2]][temp[3]] = key

ans = 0

for key, val in dic.items():
    for y in range(N):
        for x in range(N):
            if List[y][x] == key:
                like_cnt = 0
                for i in range(4):
                    yy = y + dy[i]
                    xx = x + dx[i]
                    if 0 <= yy < N and 0 <= xx < N and List[yy][xx] in val:
                        like_cnt += 1
            else:
                continue
    if like_cnt == 0:
        continue
    else:
        ans += pow(10, like_cnt-1)

print(ans)
