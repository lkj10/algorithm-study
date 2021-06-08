#!/usr/bin/env python
# coding: utf-8

# In[2]:


#2주차-프로그래머스 해쉬
#완주하지 못한 선수
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i]!=completion[i]:
            return participant[i]
    return participant[-1]
solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"])


# In[3]:


#전화번호 목록
def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
            break
    return answer
solution(["119", "97674223", "1195524421"])


# In[ ]:


#위장
def solution(clothes):
    adic={}
    answer = 0
    for i in clothes:
        if i[1] in adic:
            adic[i[1]]+=1
        else:
            adic[i[1]]=1
    cnt=1
    for i in adic.values():
        cnt*=(i+1)
    return cnt-1
solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])

