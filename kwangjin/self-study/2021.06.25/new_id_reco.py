def solution(new_id):
    answer = ''
    List = list(new_id)
    temp = list()
    temp2 = list()
    cnt = 0
    #step 1
    for i in range(len(List)):
        if List[i].isalpha():
            List[i] = List[i].lower()
            
    #step 2
    for i in range(len(List)):
        if List[i].isalpha() or List[i].isdecimal() or List[i] == '-' or List[i] == '_' or List[i] == '.':
            temp.append(List[i])
    #step 3
    for i in temp:
        temp2.append(i)
        if i == '.':
            cnt += 1
            if cnt == 2:
                temp2.pop()
                cnt = 1
        else:
            cnt = 0
            
    #step 4
    if temp2 and temp2[0] == '.' :
        temp2.pop(0)
    if temp2 and temp2[-1] == '.':
        temp2.pop()
        
    #step 5
    if temp2 == []:
        temp2.append('a')
    
    #step 6
    if len(temp2) >= 16:
        temp2 = temp2[:15]
        if temp2[-1] == '.':
            temp2.pop()
    
    #step 7
    if len(temp2) <= 2:
        temp_str = temp2[-1]
        while len(temp2) < 3:
            temp2.append(temp_str)

    return ''.join(temp2)