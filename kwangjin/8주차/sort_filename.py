import re


def solution(files):
    answer = []
    List = list()
    for file in files:
        B = re.search('\d+', file)
        HEAD = file[:B.span()[0]]
        NUMBER = B.group()
        TAIL = file[B.span()[1]:]
        List.append((HEAD, NUMBER, int(NUMBER), TAIL))
    List.sort(key=lambda x: (x[0].lower(), x[2]))
    for i in List:
        answer.append(i[0]+i[1]+i[3])
    return answer
