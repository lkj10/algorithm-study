import sys
import heapq
sys.stdin=open("input.txt", "r")

T = int(input())
for _ in range(T):
    k = int(input())
    MAX_List = list()
    MIN_List = list()
    List = list()
    for i in range(k):
        M, N = map(str, input().split())
        if M == 'I':
            heapq.heappush(MAX_List, -int(N))
            heapq.heappush(MIN_List, int(N))
        elif M == 'D':
            if len(MAX_List) == 0 or len(MIN_List) == 0 :
                continue
            if int(N) == 1:
                List.append(heapq.heappop(MAX_List)*-1)
            elif int(N) == -1:
                List.append(heapq.heappop(MIN_List))

            if len(MAX_List) == 0 or len(MIN_List) == 0 :
                MAX_List.clear()
                MIN_List.clear()

    for i in List:
        if -i in MAX_List:
            MAX_List.pop(MAX_List.index(-i))
        if i in MIN_List:
            MIN_List.pop(MIN_List.index(i))
    
    if len(MAX_List + MIN_List) > 0 :
        print(heapq.heappop(MAX_List)*-1, heapq.heappop(MIN_List))
    else:
        print("EMPTY")




