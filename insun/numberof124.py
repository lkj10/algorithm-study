# https://programmers.co.kr/learn/courses/30/lessons/12899
def solution(n):
    answer = ''
    while n > 0:
        # 1. 3으로 나눠지는 경우.
        if n % 3 == 0:
            # 3으로 나눠지는 경우 항상 4로 끝남.
            answer = '4' + answer
            n = int(n / 3) - 1  # 몫은 3으로 나눈 후 -1을 해야 한다.
        else:
            # 3으로 나눠지지 않는 경우에는 n을 3으로 나눈 후 나머지를 answer과 더한다.
            answer = str(n % 3) + answer
            n = int(n / 3)  # 몫 저장

    return answer
