def solution(answers):
    
    answer = []
    NUM_1 = [1, 2, 3, 4, 5]
    NUM_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    NUM_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    cnt = [0, 0, 0]
    
    for i in range(len(answers)):
        if answers[i] == NUM_1[i%len(NUM_1)]:
            cnt[0] += 1
        if answers[i] == NUM_2[i%len(NUM_2)]:
            cnt[1] += 1
        if answers[i] == NUM_3[i%len(NUM_3)]:
            cnt[2] += 1
    
    MAX = max(cnt)
    
    for idx, val in enumerate(cnt):
        if MAX == val:
            answer.append(idx+1)

    return answer