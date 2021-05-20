import sys
import heapq
sys.stdin = open("input.txt", "r")

T = int(input())

List = list()

for i in range(T):
    heapq.heappush(List, int(input()))

for i in range(T):
    print(heapq.heappop(List))
