def solution(participant, completion):
    answer = 0
    result = participant + completion
    dict = {}
    for i in result:
        if i in dict.keys():
            dict[i] += 1
        else:
            dict[i] = 1
    for x, y in dict.items():
        if y % 2 == 1:
            answer = x
            break
    return answer

def solution(participant, completion):
    answer = 0
    result = participant + completion
    dict = {}
    for i in result:
        dict[i] = dict.get(i, 0) + 1
    for key, val in dict.items():
        if val % 2 == 1 :
            answer = key
            break
    return answer
