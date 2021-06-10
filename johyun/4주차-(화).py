#!/usr/bin/env python
# coding: utf-8

# In[1]:
# 안녕하세요


#크레인 인형뽑기
#첫번째 시도: 테스트2,9 실패
def solution(board, moves):
    answer = 0
    bucket= []
    
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1]!= 0:
                bucket.append(board[i][m-1])
                board[i][m-1] = 0
                break
            if len(bucket)>=2 and bucket[-2]==bucket[-1]:  #if문 안에 있으면 break를 만나서 아래 코드가 실행되지 않음
                bucket.pop()
                bucket.pop()
                answer+=2  
    return answer


# In[ ]:


#모의고사
def solution(answers):
    answer = []
    scores = [0, 0, 0]
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == pattern1[i % len(pattern1)]:  #i%len(pattern_)을 생각하는데에 시간이 오래걸림. 인덱스와 개수의 시작점의 차이를 이용하는 방식 잘 기억해두자.
            scores[0] += 1
        if answers[i] == pattern2[i % len(pattern2)]:
            scores[1] += 1
        if answers[i] == pattern3[i % len(pattern3)]:
            scores[2] += 1

    max_score = max(scores)
    for i in range(3):
        if scores[i] == max_score:
            answer.append(i+1)
    return answer

