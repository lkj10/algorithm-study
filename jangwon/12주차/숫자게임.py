def solution(A, B):
    result = 0
    A.sort()
    B.sort()
    idx = 0
    
    for i in range(len(A)):
        if A[idx] < B[i]:
            result += 1
            idx += 1
    return result