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
