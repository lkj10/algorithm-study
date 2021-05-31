# 체육복
# 어떻게 풀어야 할까?
# 프로그래머스
# https://programmers.co.kr/learn/courses/30/lessons/42862?language=python3
# 난이도 : 레벨 1
# 알고리즘 종류 : 그리디 알고리즘

def solution(n, lost, reserve):
    # 여분이 있는데 도난 당한 경우에는 여분에서 제거
    reserve_change = list(set(reserve) - set(lost))
    # 도난 당한 후 여분을 사용할것이므로 도난리스트에서 제거
    lost_change = list(set(lost) - set(reserve))

    # 왼쪽부터 비교해서 도난 리스트에서 제거
    for i in reserve_change:
        if i - 1 in lost_change:
            lost_change.remove(i - 1)
        elif i + 1 in lost_change:
            lost_change.remove(i + 1)
    return n - len(lost_change)