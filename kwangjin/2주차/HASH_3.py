def solution(clothes):
    answer = 1
    dic = {}
    List = list()
    for i in clothes:
        dic[i[1]] = dic.get(i[1], 0) + 1
    
    for key, val in dic.items():
        answer *= (val+1)
        
    answer -= 1
    
    return answer
