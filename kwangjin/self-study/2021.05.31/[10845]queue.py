import sys
from collections import deque
sys.stdin = open("input.txt", "r")

T = int(sys.stdin.readline())
Dq = deque()

for _ in range(T):
    M = list(sys.stdin.readline().split())
    if M[0] == "push" :
        Dq.append(int(M[1]))
    elif M[0] == "front" :
        print(Dq[0] if Dq else -1)
    elif M[0] == "back" :
        print(Dq[-1] if Dq else -1)
    elif M[0] == "pop" :
        print(Dq.popleft() if Dq else -1)
    elif M[0] == "size":
        print(len(Dq) if Dq else 0)
    elif M[0] == "empty":
        print(0 if Dq else 1)
