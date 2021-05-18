import collections
def solution(participant, completion):
    
    # 해시 두 개 생성 Counter 모듈 사용
    participant_hash = collections.Counter(participant)
    completion_hash = collections.Counter(completion)
    
    for v in completion_hash:
        if v in participant_hash:
            # 동명이인 처리를 위해 hash2의 value를 사용
            participant_hash[v] -= completion_hash[v]
    
    return participant_hash.most_common(1)[0][0]

# 궁금증 in 문의 시간 복잡도