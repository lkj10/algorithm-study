def solution(msg):
    answer = []
    cnt = 1
    dic = {}
    
    for i in range(65, 91):
        dic[chr(i)] = cnt
        cnt += 1
    temp = ''
    
    for i in msg:
        temp += i
        if dic.get(temp):
            continue
        else:
            if dic.get(temp[:-1]):
                answer.append(dic[temp[:-1]])
                dic[temp] = cnt
                cnt += 1
                temp = temp[-1]
        
    answer.append(dic[temp])
    
    return answer