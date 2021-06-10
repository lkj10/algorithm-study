def solution(scoville, K):
    import heapq
    answer = 0

    heapq.heapify(scoville)
    temp = heapq.heappop(scoville)

    while temp <= K:
        if not scoville:
            return -1
        heapq.heappush(scoville, temp + heapq.heappop(scoville) * 2)
        temp = heapq.heappop(scoville)
        answer += 1

    return answer
