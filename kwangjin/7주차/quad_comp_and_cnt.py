def solution(arr):
    answer = [0, 0]

    def f(Len, start_x, start_y):
        temp_0, temp_1 = 0, 0
        for i in range(start_y, start_y + Len):
            for j in range(start_x, start_x + Len):
                if arr[i][j] == 1:
                    temp_1 += 1
                elif arr[i][j] == 0:
                    temp_0 += 1
        if temp_0 == Len**2:
            answer[0] += 1
        elif temp_1 == Len**2:
            answer[1] += 1
        else:
            dx = [start_x, start_x+Len//2, start_x, start_x+Len//2]
            dy = [start_y, start_y, start_y+Len//2, start_y+Len//2]
            for i in range(4):
                xx = dx[i]
                yy = dy[i]
                f(Len//2, xx, yy)

    f(len(arr), 0, 0)

    return answer
