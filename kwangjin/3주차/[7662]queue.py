import sys
import heapq
sys.stdin=open("input.txt", "r")

T = int(input())
for _ in range(T):
    k = int(input())
    MAX_List = list()
    MIN_List = list()
    dic = {}
    result = list()
    temp = 0
    for i in range(k):
        M, N = map(str, input().split())
        if M == 'I':
            heapq.heappush(MAX_List, -int(N))
            heapq.heappush(MIN_List, int(N))
            dic[int(N)] = 1
        elif M == 'D':
            if len(MAX_List) == 0 or len(MIN_List) == 0 :
                continue
            if int(N) == 1:
                temp = heapq.heappop(MAX_List)*-1
                dic[temp] = 0
            elif int(N) == -1:
                temp = heapq.heappop(MIN_List)
                dic[temp] = 0
            # if len(MAX_List) == 0 or len(MIN_List) == 0 :
            #     MAX_List.clear()
            #     MIN_List.clear()
    for idx, val in dic.items():
        if val == 1:
            result.append(idx)
            
    if len(result) > 1 :
        print(max(result), min(result))
    else:
        print("EMPTY")




