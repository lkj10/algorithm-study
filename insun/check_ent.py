def solution(n, times):
    left = 0  # 최 저 시간
    answer = right = max(times) * n  # 최 대 시간  10 * 60

    while left <= right:
        complete = 0  # 심사 처리 수
        mid = (left + right) // 2  # 이분 탐색, 중간부터 탐색 시작

        for r in times:
            complete += mid // r

        if complete < n:  # 처리수가 입국심사를 기다리는 수보다 작을 경우
            left = mid + 1  # 중간 값 + 1
        else:
            right = mid - 1  # 아닐경우 -1
            if mid <= answer:  # 이전에 저장한 심사시간보다 작을 경우 갱신
                answer = mid
    return answer