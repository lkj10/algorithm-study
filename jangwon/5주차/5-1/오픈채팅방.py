import collections

def solution(record):
    answer = []
    hash_table = collections.defaultdict(str)
    record = [r.split() for r in record]
    
    # 최종적으로 바뀐 아이디
    for r in record:
        attr = r[0]
        u_id = r[1]
        if attr == 'Enter':
            hash_table[u_id] = r[2]
        elif attr == 'Change':
            hash_table[u_id] = r[2]
            
    # record 확인 
    for r in record:
        attr = r[0]
        u_id = r[1]
        if attr == 'Enter':
            answer.append(f'{hash_table[u_id]}님이 들어왔습니다.')
        elif attr == 'Leave':
            answer.append(f'{hash_table[u_id]}님이 나갔습니다.')
            
    return answer

def solution1(record):
    result = []
    dic = {}
    stack = []
    record = [r.split() for r in record]
    
    for r in record:
        attr = r[0]
        u_id = r[1]
        # 첫 입장
        if attr == 'Enter':
            # 재 입장
            for s in stack:
                if s[0] == u_id:
                    if s[1].find('나갔습니다.') != -1:
                        s[1] = f'{r[2]}님이 나갔습니다.'
                    else:
                        s[1] = f'{r[2]}님이 들어왔습니다.'
                        
            dic[u_id] = f'{r[2]}님이 들어왔습니다.'
            stack.append([u_id,dic[u_id]])
        # 떠나는 경우
        elif attr == 'Leave':
            leave_comment = dic[u_id].replace('들어왔습니다.', '나갔습니다.')
            stack.append([u_id,leave_comment])
        # 바꾸는 경우
        elif attr == 'Change':
            for s in stack:
                if s[0] == u_id:
                    s[1] = f'{r[2]}님이 들어왔습니다.'
                    
    for s in stack:
        result.append(s[1])

    return result

# 시간 복잡도 O(N^3)
# 심각한 뻘짓
# 결론적으로 테스트케이스만 통과 시간복잡도 흘러 넘침

