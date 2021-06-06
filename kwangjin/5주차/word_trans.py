def solution(begin, target, words):
    answer = []
    visit = [0] * len(words) 
    dic = {begin : []}
    
    for i in words:
        dic[i] = []
        
    for i in dic:
        for j in words:
            cnt = 0
            for k in range(len(begin)):
                if i[k] == j[k]:
                    cnt += 1
            if cnt == len(begin) - 1:
                dic[i].append(j)
                
    def DFS(L, word):
        if word == target:
            answer.append(L)
        else:
            for i in dic[word]:
                if visit[words.index(i)] == 0:
                    visit[words.index(i)] = 1
                    DFS(L+1, i)
                    visit[words.index(i)] = 0
                    
    if target in words:
        DFS(0, begin)
        
    else:
        return 0
    
    return min(answer)