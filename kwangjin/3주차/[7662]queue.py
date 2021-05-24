import sys
import heapq
sys.stdin=open("input.txt", "r")

T = int(input())
for _ in range(T):
    k = int(input())
    MAX_List = list()
    MIN_List = list()
    dic = {}

    for i in range(k):
        M, N = map(str, input().split())
        if M == 'I':
            heapq.heappush(MAX_List, (-int(N), i))
            heapq.heappush(MIN_List, (int(N), i))
            dic[i] = 1
        elif M == 'D':
            if int(N) == 1:
                while MAX_List and dic[MAX_List[0][1]] == 0:
                    heapq.heappop(MAX_List)
                if MAX_List:
                    dic[MAX_List[0][1]] = 0
                    heapq.heappop(MAX_List)
            elif int(N) == -1:
                while MIN_List and dic[MIN_List[0][1]] == 0:
                    heapq.heappop(MIN_List)
                if MIN_List:
                    dic[MIN_List[0][1]] = 0
                    heapq.heappop(MIN_List)

    while MAX_List and dic[MAX_List[0][1]] == 0:
        heapq.heappop(MAX_List)
    while MIN_List and dic[MIN_List[0][1]] == 0:
        heapq.heappop(MIN_List)

    if MAX_List and MIN_List :
        print(heapq.heappop(MAX_List)[0]*-1, heapq.heappop(MIN_List)[0])
    else:
        print("EMPTY")






