import sys
from collections import deque
sys.stdin = open("input.txt", "r")

n, w, L = map(int, input().split())

List = deque(map(int, input().split()))
dq = deque()
time = 0

for i in List:
    time += 1
    if sum(dq) + i < L :
        dq.append(i)
    else:
        while sum(dq) > L  :
            dq.popleft()
            time += 1

print(dq)
print(time)