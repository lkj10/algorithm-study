# 숫자 게임 : https://programmers.co.kr/learn/courses/30/lessons/12987
def solution(A, B):
    answer = 0
    A = sorted(A)
    B = sorted(B)
    score_a = score_b = len(A) - 1
    while score_a >= 0:
        if A[score_a] < B[score_b]:
            answer += 1
            score_b -= 1
        score_a -= 1
    return answer
