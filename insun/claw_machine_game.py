# 프로그래머스 - 크레인 인형뽑기 게임 - 레벨 1
# https://programmers.co.kr/learn/courses/30/lessons/64061

# 내 풀이
def solution(board, moves):
    answer = 0
    basket = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] == 0:
                pass
            else:
                basket.append(board[j][i - 1])
                board[j][i - 1] = 0
                break
        if len(basket) >= 2 and (basket[len(basket) - 1] == basket[len(basket) - 2]):
            basket.pop(-1)
            basket.pop(-1)
            answer += 1
    return answer * 2


# board_test = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
# moves_test = [1, 5, 3, 5, 1, 2, 1, 4]
# print(solution(board_test, moves_test))

# 다른 사람 풀이
def solution2(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] != 0:
                stacklist.append(board[j][i - 1])
                board[j][i - 1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2
                break

    return answer
