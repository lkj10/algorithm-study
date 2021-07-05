def solution(arr):
    answer = [0, 0]
    N = len(arr)

    def comp(x, y, n):
        init = arr[x][y]  # 해당 네모값중 하나 # 모두 같아야 통과임
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != init:  
                    div = n // 2
                    comp(x, y, div)
                    comp(x, y + div, div)
                    comp(x + div, y, div)
                    comp(x + div, y + div, div)
                    return
        
        answer[init] += 1

    comp(0, 0, N)
    return answer