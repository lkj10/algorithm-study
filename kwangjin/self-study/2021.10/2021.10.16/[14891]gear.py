import sys
from collections import deque

sys.stdin = open("input.txt", "r")

# N 극은 0, S극은 1
# 12시 부터 시계방향으로 주어짐
# 2번과 6번이 다른 톱니바퀴와 맞닿는 번호 
List = [deque(map(int, input())) for _ in range(4)]

K = int(input())

for _ in range(K):
    N, D = map(int, input().split())
    rotate = [0, 0, 0, 0] # 0이면 회전 x 1이면 시계방향, -1이면 반시계
    rotate[N-1] = D
    #for문으로 왼쪽 오른쪽 나눠야함
    for i in range(N-2, -1, -1): #왼쪽은 6번을 봐야함
        if List[i+1][6] != List[i][2] : #바꾸기 전에 두개가 다르다면 그 번호 회전.
            rotate[i] = rotate[i+1]*-1
        else: # 다르면 for문 탈출
            break
    for i in range(N-1, 3): #오른쪽은 2번을 봐야함 본체는 2번 마주보는건 6번!
        if List[i][2] != List[i+1][6] : #바꾸기 전에 두개가 다르다면 그 번호 회전.
            rotate[i+1] = rotate[i]*-1
        else: # 다르면 for문 탈출
            break
    for i in range(4):
        if rotate[i] == 1:
            List[i].appendleft(List[i].pop())
        if rotate[i] == -1:
            List[i].append(List[i].popleft())

ans = 0
for i in range(4):
    if List[i][0] == 1:
        ans += pow(2, i)

print(ans)

