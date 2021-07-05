def solution(n):
    answer = []
    List = [[0]*(i+1) for i in range(n)]
    cnt = 0
    SUM = 0
    k = 0
    down, right, up = n, n-1, n-2

    for i in range(1, n+1):
        SUM += i

    while 1:

        for i in range(down):  # 아래 방향
            cnt += 1
            List[2*k + i][0 + k] = cnt

        down -= 3
        if cnt == SUM:
            break

        for i in range(right):  # 오른쪽 방향
            cnt += 1
            List[n-1-k][k+1+i] = cnt

        right -= 3
        if cnt == SUM:
            break

        for i in range(up):  # 윗 방향
            cnt += 1
            List[n-2-k-i][n-2-2*k-i] = cnt

        up -= 3
        if cnt == SUM:
            break
        k += 1

    for i in List:
        answer += i

    return answer
