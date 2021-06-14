#!/usr/bin/env python
# coding: utf-8

# In[1]:


#체육복
def solution(n, lost, reserve): 
    Lreserve=set(reserve)-set(lost)
    Lreserve2=Lreserve
    Llost=set(lost)-set(reserve)
    Llost2=Llost
    answer=0
    for i in list(Llost2):  #런타임에러나서 list로 씌워주긴했는데...
        if i-1 in list(Lreserve2):
            Llost.remove(i)
            Lreserve.remove(i-1)  #한번 빌려주면 또 빌려줄수없으므로 삭제
        elif i+1 in list(Lreserve2):
            Llost.remove(i)
            Lreserve.remove(i+1) 
    answer = n-len(Llost) 
    return answer

