
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while True:

        if scoville[0]>=K:
            break
        if len(scoville)<2:
            break
        a=heapq.heappop(scoville)
        b=heapq.heappop(scoville)
        score = a+(b*2)
        heapq.heappush(scoville,score)
        answer+=1
    #print(scoville)

    if max(scoville)<K:
        return -1
    else:
        return answer