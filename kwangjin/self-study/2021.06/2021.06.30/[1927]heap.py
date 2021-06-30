import sys
import heapq
sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())

List = list()

for i in range(N):
    A = int(sys.stdin.readline())
    if A == 0:
        print(heapq.heappop(List) if List else 0)
    else:
        heapq.heappush(List, A)


