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
            print(res[1])

        else:
            print(0)

    else:
        if temp < 0 :
            temp = temp * -1    
            heapq.heappush(List, (temp, -temp))
        else:
            heapq.heappush(List, (temp, temp))
