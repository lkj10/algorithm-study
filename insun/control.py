# https://programmers.co.kr/learn/courses/30/lessons/12973
# 짝지어 제거하기
# 모두 제거하는 경우 찍지어 제거 하기가 종료된다.
# 모두 제거가 되는 경우에는 1이고, 아닐 경우에는 0을 리턴한다
# 될 경우랑 안 될경우를 모두 고려해야 한다.
# 스택을 사용한다.
# 스텍에 값이 있는 경우에는 그 전값과 비교, 값이 없는 경우에는 append


# 시작시간:
def solution(s):
    number = []
    for i in s:
        if number:
            if number[-1] == i:
                number.pop()
            else:
                number.append(i)
        else:
            number.append(i)
    if number:
        return 0
    else:
        return 1
