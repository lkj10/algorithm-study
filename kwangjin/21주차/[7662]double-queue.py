import sys
import heapq
sys.stdin = open("input.txt", "r")


T = int(input())

for _ in range(T):
    k = int(input())
    min_hq = []
    max_hq = []
    cnt = 0
    dic = {}
    for idx in range(k):
        cmd, n = input().split()
        if cmd == 'I':
            cnt += 1
            heapq.heappush(max_hq, (int(n), idx))
            heapq.heappush(min_hq, (-int(n), idx))
            dic[idx] = 1
        if cmd == 'D':
            if cnt < 1:
                continue
            if n == '1':
                while min_hq and dic[min_hq[0][1]] == 0:
                    heapq.heappop(min_hq)
                if min_hq:
                    dic[min_hq[0][1]] = 0
                    heapq.heappop(min_hq)
            if n == '-1':
                while max_hq and dic[max_hq[0][1]] == 0:
                    heapq.heappop(max_hq)
                if max_hq:
                    dic[max_hq[0][1]] = 0
                    heapq.heappop(max_hq)
            cnt -= 1
    if cnt < 1:
        print("EMPTY")
        continue    
    while min_hq and dic[min_hq[0][1]] == 0:
        heapq.heappop(min_hq)
    while max_hq and dic[max_hq[0][1]] == 0:
        heapq.heappop(max_hq)
    print(heapq.heappop(min_hq)[0] * -1, heapq.heappop(max_hq)[0])
    

# -45 -642 45 
# -45 45 333 

# max 45 -653/ 642 -45 -97/

# min -45/ 653/ -642 45 97