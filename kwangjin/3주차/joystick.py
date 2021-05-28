def solution(name):
    
    answer = 0
    now = 0
    
    List = list()
    visit = [0] * len(name)
    
    
    for i in range(len(name)):
        List.append(ord(name[i]) - 65)
        if ord(name[i]) - 65 == 0:
            visit[i] = 1
        
    
    while True:
        
        left = 0
        right = 0
        
        visit[now] = 1

        if List[now] > 13:
            answer += 26 - List[now]
        else:
            answer += List[now]
        
        if sum(visit) == len(name):
            break
            
        while True:
            left -= 1
            right += 1
            
            # if now == len(name) - 1:
            #     now = -1
                
            if List[now+right] > 0 and visit[now+right] == 0 :
                answer += right
                now += right
                break
                
            elif List[now+left] > 0 and visit[now+left] == 0 :
                answer += abs(left)
                now += left
                break

    return answer