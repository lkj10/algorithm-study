def solution(board, moves):
    answer = 0
    bowl = list()
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] > 0:
                temp, board[j][i-1] = board[j][i-1], 0
                break
        else:
            temp = 0
            
        if bowl and bowl[-1] == temp:
            bowl.pop()
            answer += 2
            
        elif temp > 0:
            bowl.append(temp)
            
    return answer