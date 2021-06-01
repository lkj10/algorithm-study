def solution(board, moves):
    answer = 0
    box = []
    for move in moves:
        pick = crain(board, move)
        # move 위치에 인형이 있을 경우
        if pick:
            # 박스가 비었을 경우
            if not box:
                box.append(pick)
            else:
                # box 맨위에 값이랑 같을 경우 박스 맨 위에 값 삭제 후 answer + 1
                if pick == box[-1]:
                    box.pop()
                    answer += 1
                # box 위에 값이랑 다를 경우
                else:
                    box.append(pick)

    return answer * 2


def crain(board, move):
    count = 0
    box = []
    length = len(board)
    for i in range(length):
        for j in range(length):
            # move 위치의 값 선택
            if j == move - 1 and board[i][j] != 0:
                pick = board[i][j]
                board[i][j] = 0
                return pick

    # 해당 칸에 값이 없는 경우
    return 0