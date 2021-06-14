def solution(board, moves):
    result = 0
    stack = []
    
    for move in moves:
        for i, b in enumerate(board):
            # 인형이 있는 경우
            if board[i][move - 1] != 0:
                # 인형을 뽑고 0으로 처리 해야하기 때문에 임시 값 선언
                tmp = board[i][move - 1]
                # 인형을 뽑고 0으로 처리
                board[i][move - 1] = 0
                if len(stack) > 0 and stack[-1] == tmp:
                    stack.pop()
                    result += 2
                else:
                    stack.append(tmp)
                # 처리 했으면 반복문 중지 
                break
    
    return result