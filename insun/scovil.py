# 시간 초과 함.
# from collections import deque
def solution(scoville, K):
    answer = 0

    # min은 n..
    # while 문 -> n^2
    while min(scoville) < K:
        # break 조건: 스코빌 지수가 하나 남고
        # K보다 작으면 -1  n^2 이넘음....1,000,000,000
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        # sorted >> nlogn
        scoville = sorted(scoville, reverse=True)

        scoville.append(scoville.pop() + scoville.pop() * 2)

        answer += 1

    return answer