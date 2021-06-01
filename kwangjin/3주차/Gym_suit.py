def solution(n, lost, reserve):
    answer = 0
    dic = {}#List로 만들어도 됨
    for i in range(1, n+1):
        dic[i] = 1
        
    for i in lost:
        dic[i] -= 1
        
    for i in reserve:        
        dic[i] += 1

    for i in range(2, n+1):
        if dic[i] == 2 and dic[i-1] == 0:
            dic[i] -= 1
            dic[i-1] += 1
            
    for i in range(1, n):
        if dic[i] == 2 and dic[i+1] == 0:
            dic[i] -= 1
            dic[i+1] += 1
            
    answer = len([x for x in dic.values() if x != 0])
            
    return answer