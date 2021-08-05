def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    pivot_b = 0
    for idx_a in range(len(A)):
        for idx_b in range(pivot_b, len(B)):
            if B[idx_b] > A[idx_a]:
                pivot_b = idx_b + 1
                answer += 1
                break
    return answer