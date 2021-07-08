import collections
def solution(board):
    result = 0
    n = len(board)
    m = len(board[0])
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    Q = collections.deque()
    Q.append((0, 0))
    
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (nx >= 0 and ny >= 0 and nx < n and ny < m):
                if (board[nx][ny] == 1):
                    board[nx][ny] = board[x][y] + 1
                    Q.append((nx, ny))
    
    if board[n - 1][m - 1] == 1:
        return -1
    else:
        return board[n - 1][m - 1]
    
                