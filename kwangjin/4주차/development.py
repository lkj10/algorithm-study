def solution(progresses, speeds):
    from collections import deque
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    cnt = 0

    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        if progresses[0] >= 100:
            while progresses and progresses[0] >= 100:
                progresses.popleft()
                speeds.popleft()
                cnt += 1
            answer.append(cnt)
            cnt = 0

    return answer
