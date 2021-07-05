import sys
from collections import deque
sys.stdin = open("input.txt", "r")


# 이런 문제는 DFS를 하면 안된다!
# visit함수를 쓰면 되지만
# 백준에선 메모리초과 이슈가 뜨므로
# BFS로 해야함!

M, N = map(int, input().split())

List = [100001] * (100001)
dq = deque()
dq.append((M, 0))

while dq:
    temp = dq.popleft()
    if temp[0] == N:
        List[temp[0]] = temp[1]
        break
    if 100001> temp[0] >= 0 and List[temp[0]] > temp[1]:
        List[temp[0]] = temp[1]
        dq.append((temp[0]-1, temp[1]+1))
        dq.append((temp[0]+1, temp[1]+1))
        dq.append((temp[0]*2, temp[1]+1))

print(List[N])