import collections


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


# 두번째 풀이 - collection.Counter()를 사용
# Counter()는 리스트 원소들의 개수를 알고 싶을 때 사용 가능
def solution2(participant, completion):
    answer2 = collections.Counter(participant) - collections.Counter(completion)
    return list(answer2.keys())[0]
