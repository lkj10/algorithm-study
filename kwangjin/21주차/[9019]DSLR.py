import sys
from collections import deque

sys.stdin = open("input.txt", "r")

def bfs():
    visit = [0]*10000
    while dq:

        cmd, A = dq.popleft()
        visit[A] = 1

        if A == B:
            print(cmd)
            return

        if visit[(A*2)%10000] == 0: # D
            visit[(A*2)%10000] = 1
            dq.append((cmd+'D', (A*2)%10000))
        
        if A == 0 and visit[9999] == 0: # S
            visit[9999] = 1
            dq.append((cmd+'S', 9999))
        elif visit[A-1] == 0:
            visit[A-1] = 1
            dq.append((cmd+'S', A-1))

        if visit[A%1000 * 10 + A//1000] == 0: # L
            visit[A%1000 * 10 + A//1000] = 1
            dq.append((cmd+'L', A%1000 * 10 + A//1000))
        
        if visit[A//10 + A%10 * 1000] == 0: # R
            visit[A//10 + A%10 * 1000] = 1
            dq.append((cmd +'R', A//10 + A%10 * 1000))


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    dq = deque()
    dq.append(('',A))
    bfs()


