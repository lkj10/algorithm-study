def solution(str1, str2):
    
    answer = 0
    
    List_str1 = list()
    List2_str1 = list()
    List_str2 = list()
    List2_str2 = list()
    two_in = 0 # 교집합
    SUM = 0 # 합집합
    dic = {}
    
    for i in range(1, len(str1), 2):
        List_str1.append(str1[i-1:i+1])
        List_str1.append(str1[i:i+2])
        
    for i in range(1, len(str2), 2):
        List_str2.append(str2[i-1:i+1])
        List_str2.append(str2[i:i+2]) 
    
    if len(str1)%2 == 0:
        List_str1.pop()
        
    if len(str2)%2 == 0:
        List_str2.pop()
    
    
    for i in List_str1:
        if i.isalpha():
            List2_str1.append(i.lower())
            
    for i in List_str2:
        if i.isalpha():
            List2_str2.append(i.lower())
            
    print(List2_str1, List2_str2)

    for i in List2_str1:
        if i not in dic:
            dic[i] = [1, 0]
        else:
            dic[i][0] += 1
            
    for i in List2_str2:
        if i not in dic:
            dic[i] = [0, 1]
        else:
            dic[i][1] += 1
            

    for val in dic.values():
            SUM += max(val) 
            two_in += min(val)
            
    if len(dic) > 0:
        
        answer = int((two_in/SUM)*65536)
    else:
        answer = 65536

    return answer