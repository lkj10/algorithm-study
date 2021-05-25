def solution(n, lost, reserve):
    answer = 0
    array = [0] * 30
    for i in range(n):
        array[i] = 1
    for i in lost:
        array[i - 1] -= 1

    for i in reserve:
        array[i - 1] += 1

    for i in range(n):
        if array[i] > 1:

            # 양 옆이 0인 경우
            if i + 1 < n and array[i + 1] == 0 and i - 1 >= 0 and array[i - 1] == 0:
                if array[i + 2] > 1:
                    if array[i - 1] == 0 and array[i] > 1:
                        array[i - 1] = 1
                        array[i] = 1

            # 한쪽만 0 인 경우
            if i - 1 >= 0 and array[i - 1] == 0:
                if array[i - 1] == 0 and array[i] > 1:
                    array[i - 1] = 1
                    array[i] = 1

            if i + 1 < n and array[i + 1] == 0:
                if array[i + 1] == 0 and array[i] > 1:
                    array[i + 1] = 1
                    array[i] = 1

    for i in array:
        if i:
            answer += 1

    return answer