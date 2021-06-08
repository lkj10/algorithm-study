import sys
from collections import deque
sys.stdin = open("input.txt", "r")

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    List = list(map(int, input().split()))
    result = deque()
    for i in range(N):
        result.append((List[i], i))
    result_M = result[M]
    cnt = 0
    while result:
        tmp = result[0]
        if tmp != max(result, key=lambda x: (x[0])):
            result.append(result.popleft())
        else:
            cnt += 1
            if result_M == result.popleft():
                break
    print(cnt)
