import sys
import heapq
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    visited = [False] * 1000001
    inputCnt = int(input())
    minHeapq = []
    maxHeapq = []
    check=0
    for i in range(inputCnt):
        command, num = input().split()
        num = int(num)
        if command == "I":
            check+=1
            heapq.heappush(minHeapq, (num,i))
            heapq.heappush(maxHeapq, (-num,i))
            visited[i] = True
        else:
            if num == 1 and maxHeapq:
                while maxHeapq and visited[maxHeapq[0][1]]==False:
                    heapq.heappop(maxHeapq)
                if maxHeapq:
                    tmp =heapq.heappop(maxHeapq)
                    visited[tmp[1]] = False

            elif num == -1 and minHeapq:
                while minHeapq and visited[minHeapq[0][1]]==False:
                    heapq.heappop(minHeapq)
                if minHeapq:
                    tmp = heapq.heappop(minHeapq)
                    visited[tmp[1]] = False



    while maxHeapq and visited[maxHeapq[0][1]] == False:
        heapq.heappop(maxHeapq)

    while minHeapq and visited[minHeapq[0][1]] == False:
        heapq.heappop(minHeapq)

    if maxHeapq and minHeapq:
        print(-maxHeapq[0][0],minHeapq[0][0])

    else:
        print("EMPTY")


'''
2
7
I 16
I -5643
D -1
D 1
D 1
I 123
D -1
9
I -45
I 653
D 1
I -642
I 45
I 97
D 1
D -1
I 333
'''