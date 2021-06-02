def solution(answers):
    # 수포자 배열
    s1 = [1, 2, 3, 4, 5];
    s2 = [2, 1, 2, 3, 2, 4, 2, 5];
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    
    # 수포자 맞춘 개수
    c1, c2, c3 = 0, 0, 0
    
    for idx, num in enumerate(answers):
        if s1[idx % len(s1)] == num: c1 += 1
        if s2[idx % len(s2)] == num: c2 += 1
        if s3[idx % len(s3)] == num: c3 += 1
    
    max_cnt = max(c1, c2, c3)
    cnt = [c1, c2, c3]
    result = []
    
    for idx, c in enumerate(cnt):
        if max_cnt == c: result.append(idx + 1)
    
    result.sort()
    return result