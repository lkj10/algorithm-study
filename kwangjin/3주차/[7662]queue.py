import sys
import heapq
sys.stdin=open("input.txt", "r")

T = int(input())
for _ in range(T):
    k = int(input())
    MAX_List = list()
    MIN_List = list()
    for i in range(k):
        M, N = map(str, input().split())
        print(MAX_List, MIN_List)
        if M == 'I':
            heapq.heappush(MAX_List, -int(N))
            heapq.heappush(MIN_List, int(N))
        elif M == 'D':
            if len(MAX_List + MIN_List) == 0 :
                continue
            if int(N) == 1:
                heapq.heappop(MAX_List)*-1
                
            elif int(N) == -1:
                heapq.heappop(MIN_List)
    else :
        if len(MAX_List + MIN_List) > 0 :
            print(heapq.heappop(MAX_List)*-1, heapq.heappop(MIN_List))




