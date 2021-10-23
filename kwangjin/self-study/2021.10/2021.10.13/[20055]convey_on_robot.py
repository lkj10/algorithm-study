import sys
from collections import deque
sys.stdin = open("input.txt", "r")

N, K = map(int, input().split())
List = list(map(int, input().split()))
conv = deque()

for i in List:
    conv.append([i, 0])
cnt = 1

while(1):
    # first
    conv.appendleft(conv.pop()) #한 칸 회전
    
    # second
    if conv[N-1][1] == 1: #로봇이 내리는 위치에 있으면
        conv[N-1][1] = 0 # 내린다.

    for i in range(N-2, -1, -1):
        if conv[i][1] == 1 and conv[i+1][1] == 0 and conv[i+1][0] > 0:
            conv[i+1][1] = conv[i][1]
            conv[i][1] = 0
            conv[i+1][0] -= 1
    conv[N-1][1] = 0

    if conv[0][0] > 0 and conv[0][1] == 0:
        conv[0][0] -= 1
        conv[0][1] = 1

    cnt_k = 0
    for i in range(len(List)):
        if conv[i][0] == 0:
            cnt_k+= 1

    if cnt_k >= K:
        print(cnt)
        break
    cnt += 1