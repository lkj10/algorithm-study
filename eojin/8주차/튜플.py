from collections import Counter


def solution(s):
    answer = []
    num_list = []
    tpStr = ""
    for i in s:
        if (i == "," or i == "}") and tpStr:
            num_list.append(int(tpStr))
            tpStr = ""
        elif i.isalnum():
            tpStr += i
    count_dict = Counter(num_list)
    for key, value in count_dict.items():
        answer.append((key, value))
    answer.sort(key=lambda x: x[1], reverse=True)
    answer = [j[0] for j in answer]
    return answer


print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
