def solution(scores):
    answer = ''
    List = [[] for _ in range(len(scores[0]))]
    Len = [len(scores[0])]*len(scores[0])
    score = []
    for i in range(len(scores)):
        for j in range(len(scores[0])):
            List[j].append(scores[i][j])
    for i in range(len(scores)):
        if (List[i].count(max(List[i])) == 1 and List[i][i] == max(List[i])) or (List[i].count(min(List[i])) == 1 and List[i][i] == min(List[i])):
            List[i][i] = 0
            Len[i] -= 1
        score.append(sum(List[i])/Len[i])
    for i in score:
        if i >= 90:
            answer += 'A'
        elif i >= 80:
            answer += 'B'
        elif i >= 70:
            answer += 'C'
        elif i >= 50:
            answer += 'D'
        else:
            answer += 'F'
                             
    return answer