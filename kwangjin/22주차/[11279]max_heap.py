import heapq
import sys

sys.stdin = open("input.txt", "r")

List = []

N = int(sys.stdin.readline())

for _ in range(N):
    temp = int(sys.stdin.readline())
    if temp == 0:
        if List :
            res = heapq.heappop(List)
            print(-res)

        else:
            print(0)

    else:
        heapq.heappush(List, -temp)
