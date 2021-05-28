# 문제 분석
# 입력 데이터의 수, Q 적용할 연산  

# 최대 힙 , 최소 힙 구현 -> 이중 우선순위 큐
# 최대 힙 -> - 로 
# ‘D 1’는 Q에서 최댓값을 삭제하는 연산을 의미하며, ‘D -1’는 Q 에서 최솟값을 삭제하는 연산을 의미한다

import sys
import heapq
input = sys.stdin.readline

test = int(input())
for _ in range(test):
    max_heap, min_heap = [], []
    visit = [False] * 1_000_001
    order_num = int(input())
    
    for key in range(order_num):
        order = input().rsplit()
        if order[0] == 'I':
            heapq.heappush(min_heap, (int(order[1]), key))
            heapq.heappush(max_heap, (-int(order[1]), key))
            visit[key] = True

        elif order[0] == 'D':
            if order[1] == '-1': 
                while min_heap and not visit[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visit[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
            elif order[1] == '1':
                while max_heap and not visit[max_heap[0][1]]: 
                    heapq.heappop(max_heap)
                if max_heap:
                    visit[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

    while min_heap and not visit[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visit[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')