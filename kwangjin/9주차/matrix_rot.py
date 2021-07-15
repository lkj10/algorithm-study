from collections import deque
def solution(rows, columns, queries):
    answer = []
    List = [[0]*columns for i in range(rows)]
    cnt = 1
    temp = deque()
    
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]
    
    
    for i in range(rows):
        for j in range(columns):
            List[i][j] = cnt
            cnt += 1
        
    for x1, y1, x2, y2 in queries:
        x, y = x2-1, y2-2
        for i in range(4):
            while 1:
                temp.append(List[x][y])
                if (x == x2-1 and y == y1-1):
                    x -= 1
                    break
                elif (x == x1-1 and y == y1-1):
                    y += 1
                    break
                elif (x == x1-1 and y == y2-1):
                    x += 1
                    break
                elif (x == x2-1 and y == y2-1):
                    break
                else:
                    x = x + dx[i]
                    y = y + dy[i]
                    
        answer.append(min(temp))            
        temp.appendleft(temp.pop())
        
        x, y = x2-1, y2-2
        for i in range(4):
            while 1:
                List[x][y] = temp.popleft()
                if (x == x2-1 and y == y1-1):
                    x -= 1
                    break
                elif (x == x1-1 and y == y1-1):
                    y += 1
                    break
                elif (x == x1-1 and y == y2-1):
                    x += 1
                    break
                elif (x == x2-1 and y == y2-1):
                    break
                else:
                    x = x + dx[i]
                    y = y + dy[i]
        
    return answer