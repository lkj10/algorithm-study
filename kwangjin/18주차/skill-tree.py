def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        cnt = 0
        for sk in skill_tree:
            if sk in skill and skill[cnt] != sk:
                break
            elif skill[cnt] == sk:
                cnt += 1
        else:
            answer += 1
            
    return answer