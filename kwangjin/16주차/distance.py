def foo(MAP):
    dy = [-1, -1, 0, 1, 1]
    dx = [0, 1, 1, 1, 0]
    for x in range(5):
        for y in range(5):
            if MAP[x][y] == 'P':
                for i in range(5):
                    xx = x + dx[i]
                    yy = y + dy[i]
                    if 5 > xx >= 0 and 5 > yy >= 0 and MAP[xx][yy] != 'X' :
                        if i % 2 != 1:
                            if MAP[xx][yy] == 'P':
                                return 0
                            if MAP[xx][yy] == 'O':
                                xxx = xx + dx[i]
                                yyy = yy + dy[i]
                                if 5 > xxx >= 0 and 5 > yyy >= 0 and MAP[xxx][yyy] == 'P':
                                    return 0
                        elif i % 2 == 1 and MAP[xx][yy] == 'P' :
                            if i == 1:
                                if MAP[xx-1][yy] == 'X' and MAP[xx][yy+1] == 'X' : 
                                    continue
                                else:
                                    return 0
                            elif i == 3:
                                if MAP[xx-1][yy] == 'X' and MAP[xx][yy-1] == 'X' : 
                                    continue
                                else:
                                    return 0
    return 1
                            
                        

def solution(places):
    answer = []
    dy = [-1, -1, 0, 1, 1]
    dx = [0, -1, -1, -1, 0]
    for place in places:
        MAP = []
        for row in place:
            MAP.append(row)
        answer.append(foo(MAP))

                        
        
    return answer