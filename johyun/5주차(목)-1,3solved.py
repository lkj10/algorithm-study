#!/usr/bin/env python
# coding: utf-8

# In[1]:


#로또
def solution(lottos, win_nums):
    answer = []
    # num_yes = []
    # num_zero = 0
    
#     for idx, n in win_nums:
#         for j in lottos:
#             if n == j:
#                 num_yes.append(n)
#             if j == 0:
#                 num_zero +=1

    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    cnt_yes = 0
    cnt_zero = lottos.count(0)
    for i in lottos:
        if i in win_nums:
            cnt_yes += 1
    return [rank[cnt_yes + cnt_zero], rank[cnt_yes]]


# In[ ]:


#오픈채팅방
def solution(record):
    answer = []
    user_dict = {}   #딕셔너리로 유저아이디와 닉네임을 저장하는 아이디어 reference통해 얻음
    chat_log = []
    
    for r in record:
        info = r.split(" ")
        if info[0] == 'Enter':
            user_dict[info[1]] = info[2]
            chat_log.append([info[1],"님이 들어왔습니다."])
        elif info[0] == "Leave":
            chat_log.append([info[1],"님이 나갔습니다."])
        elif info[0] == 'Change':
            user_dict[info[1]] = info[2]
            # chat_log.append([info[1],"님이 들어왔습니다."])
    for log in chat_log:
        answer.append(user_dict[log[0]]+log[1])
    return answer
    # for r in record:
    #     if r.split(" ")[0] == 'Enter':
    #         answer.append("{}님이 들어왔습니다".format(r.split(" ")[2]))
    #     elif r.split(" ")[0] == 'Change':
    #         answer.append("{}님이 들어왔습니다".format(r.split(" ")[2]))
    #     elif r.split(" ")[0] == 'Leave':
    #         answer.append("{}님이 나갔습니다.".format(r.split(" ")[2]))
    
  

