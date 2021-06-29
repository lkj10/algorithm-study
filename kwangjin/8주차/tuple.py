from collections import Counter
import re


def solution(s):
    answer = []
    s = s[2:-2].replace('},{', ' ')
    List = list()
    for i in s.split():
        List.append(list(map(int, i.split(','))))
    List.sort(key=lambda x: len(x))
    answer = list(List[0])
    for i in range(len(List) - 1):
        temp = list(set(List[i+1]) - set(List[i]))
        answer.append(temp[0])
    return answer


def solution(s):
    s = Counter(re.findall('\d+', s)).most_common()
    return list(int(i[0]) for i in s)
