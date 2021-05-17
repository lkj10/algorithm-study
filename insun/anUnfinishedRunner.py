# 첫번째 풀이 - 정확성은 모두 통과, 효율성은 2개 실패
def solution(participant, completion):
    participant.sort()
    completion.sort()
    print()
    for answer in participant:
        if answer in completion:
            completion.remove(answer)
        else:
            return answer
