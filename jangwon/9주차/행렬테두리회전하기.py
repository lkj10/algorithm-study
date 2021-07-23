import collections
def solution(rows, cols, queries):
    board = [[0] * cols for i in range(rows)]
    result = []
    
    for i in range(rows):
        start = i * cols + 1
        for j in range(cols):
            board[i][j] = start + j
    
    for q in queries:
        x1, y1, x2, y2 = [x - 1 for x in q]
        
        # 큐 사용
        q = collections.deque()
        # x1 고정 y1 증가
        for i in range(0, y2- y1):
            q.append(board[x1][y1 + i])
        # x1 증가, y2 고정
        for i in range(0, x2 - x1):
            q.append(board[x1 + i][y2])
        # x2 고정, y2 감소
        for i in range(0, y2 - y1):
            q.append(board[x2][y2 - i])
        # x2 감소, y1 고정
        for i in range(0, x2 - x1):
            q.append(board[x2 - i][y1])
        
        result.append(min(q))
        q.insert(0, q.pop())
        
        for i in range(0, y2- y1):
            board[x1][y1 + i] = q.popleft()
        # x1 증가, y2 고정
        for i in range(0, x2 - x1):
            board[x1 + i][y2] = q.popleft()
        # x2 고정, y2 감소
        for i in range(0, y2 - y1):
            board[x2][y2 - i] = q.popleft()
        # x2 감소, y1 고정
        for i in range(0, x2 - x1):
            board[x2 - i][y1] = q.popleft()
            
    return result