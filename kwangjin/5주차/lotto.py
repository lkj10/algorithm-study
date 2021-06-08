def solution(lottos, win_nums):
    
    answers = [0] * 46
    result = [6, 6, 5, 4, 3, 2, 1]
    cnt = 0
    cnt_0 = 0
    
    for i in win_nums:
        answers[i] = 1
        
    for i in lottos:
        if i == 0:
            cnt_0 += 1
        if answers[i] == 1:
            cnt += 1
            
    answer = [result[cnt_0 + cnt] , result[cnt]]
    
    return answer