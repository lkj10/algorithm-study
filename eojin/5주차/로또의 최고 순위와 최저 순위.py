from collections import Counter


def solution(lottos, win_nums):
    answer = []
    match = 0
    lottosCounter = Counter(lottos)
    for key, value in lottosCounter.items():

        if key in win_nums:
            match += 1

    answer.append(ranking(match + lottosCounter[0]))
    answer.append(ranking(match))

    return answer


def ranking(match):
    if match >= 6:
        return 1
    elif match >= 5:
        return 2
    elif match >= 4:
        return 3
    elif match >= 3:
        return 4
    elif match >= 2:
        return 5
    else:
        return 6