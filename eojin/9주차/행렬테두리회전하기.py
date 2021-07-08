def solution(rows, columns, queries):

    answer=[]
    array=[[0]* columns for i in range(rows)]
    for i in range(rows):
        for j in range(columns):
            array[i][j] = i*columns+j+1

    for t, l, b, r in queries:
        top, left, bottom, right = t-1, l-1, b-1, r-1
        tmp = array[top][left]
        minimum = tmp

        for x in range(top, bottom):
            value = array[x + 1][left]
            array[x][left] = value
            minimum = min(minimum, value)

        for y in range(left, right):
            value = array[bottom][y+1]
            array[bottom][y] = value
            minimum = min(minimum, value)

        for x in range(bottom,top,-1):
            value = array[x - 1][right]
            array[x][right] = value
            minimum = min(minimum, value)

        for y in range(right,left,-1):
            value = array[top][y-1]
            array[top][y] = value
            minimum = min(minimum, value)
        array[top][left+1]=tmp
        answer.append(minimum)
    return answer
print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))