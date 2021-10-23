# 변수 초기화 확실히 할 것!
# 좌표나 변수 이름 확인 확실히 할 것!

import sys
from collections import deque
sys.stdin = open("input.txt", "r")

N, K = map(int, input().split())
dq = deque(list(map(int, input().split())))
robot = deque([0]*2*N)


def step1():
    dq.appendleft(dq.pop())
    robot.appendleft(robot.pop())
    if robot[N-1] == 1:
        robot[N-1] = 0


def step2():
    for i in range(N-2, -1, -1):
        if robot[i] == 1:
            if robot[i+1] == 0 and dq[i+1] > 0:
                robot[i+1] = 1
                dq[i+1] -= 1
                robot[i] = 0
        if robot[N-1] == 1:
            robot[N-1] = 0


def step3():
    if robot[0] == 0 and dq[0] > 0:
        robot[0] = 1
        dq[0] -= 1


def step4():
    global K
    cnt = 0
    for i in range(N*2):
        if dq[i] == 0:
            cnt += 1

    if cnt >= K:
        return -1


level = 1
while 1:
    step1()
    step2()
    step3()
    if step4() == -1:
        print(level)
        break
    level += 1
