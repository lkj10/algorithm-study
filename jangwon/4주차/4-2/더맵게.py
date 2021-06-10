import heapq
def solution(scoville, K):
    hq = []
    for s in scoville:
        heapq.heappush(hq, s)
    
    answer = []
    
    def dfs(arr, result, K):
        first = heapq.heappop(hq)
        if first > K:
            answer.append(result)
            return
        else:
            second = heapq.heappop(hq)
            result += 1
            new_scoville = first + (second * 2)
            heapq.heappush(arr, new_scoville)
            dfs(arr, result, K)
            
    dfs(hq, 0, K)
    return answer[0]
    
"""
모든 음식의 스코빌 지수가 K이상
가장 낮은 두 개의 음식을 

가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

섞어야 하는 횟수 구하기


1. 최소 힙 두 개를 구해 처리해주고 
2. 새로운 배열을 만들어 준다. 
"""

import heapq
def solution(scoville, K):
    hq = []
    for s in scoville:
        heapq.heappush(hq, s)
    
    new_arr = hq[:]
    result = 0
    
    for _ in range(len(new_arr)):
        first = heapq.heappop(new_arr)
        if first > K:
            continue
        else:
            second = heapq.heappop(new_arr)
            new_scoville = first + (second * 2)
            result += 1
            heapq.heappush(new_arr, new_scoville)
            
    return result


"""
모든 음식의 스코빌 지수가 K이상
가장 낮은 두 개의 음식을 

가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

섞어야 하는 횟수 구하기


1. 최소 힙 두 개를 구해 처리해주고 
2. 새로운 배열을 만들어 준다. 
"""