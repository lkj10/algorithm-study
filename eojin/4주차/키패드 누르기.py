array = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ["*", 0, "#"]]
keyPad = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2), 0: (3, 1)}
left = [1, 4, 7]
right = [3, 6, 9]


def solution(numbers, hand):
    answer = ''

    leftXY = (3, 0)
    rightXY = (3, 2)

    for i in numbers:
        if i in left:
            answer += "L"
            leftXY = keyPad[i]
        elif i in right:
            answer += "R"
            rightXY = keyPad[i]
        else:
            keyPos = keyPad[i]
            leftDistance = abs(leftXY[0] - keyPos[0]) + abs(leftXY[1] - keyPos[1])
            rightDistance = abs(rightXY[0] - keyPos[0]) + abs(rightXY[1] - keyPos[1])
            if leftDistance > rightDistance:
                answer += "R"
                rightXY = keyPos
            elif leftDistance < rightDistance:
                answer += "L"
                leftXY = keyPos
            else:
                if hand == "right":
                    answer += "R"
                    rightXY = keyPos
                else:
                    answer += "L"
                    leftXY = keyPos
    return answer