def solution(table, languages, preference):
    answer = ''
    dic = {}
    for tech in table:
        List = list(map(str, tech.split()))
        dic[List[0]] = []
        for i in range(1, len(List)):
            dic[List[0]].append((6-i, List[i])) 
    MAX = 0
    for tech in sorted(dic.keys()):
        SUM = 0
        for score in dic[tech]:
            for i in range(len(languages)):
                if score[1] == languages[i]:
                    SUM += preference[i] * score[0]
        if SUM > MAX:
            MAX = SUM
            answer = tech
            
    return answer