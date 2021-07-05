def solution(answers):
    answer = []
    num1 = [1,2,3,4,5]
    num1Len=5
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num2Len=8
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    num3Len=10

    answersLen = len(answers)
    num1OMR = (answersLen // num1Len) * num1 + num1[:answersLen % num1Len]
    num2OMR = (answersLen // num2Len) * num2 + num2[:answersLen % num2Len]
    num3OMR = (answersLen // num3Len) * num3 + num3[:answersLen % num3Len]

    num1Count=0
    num2Count=0
    num3Count=0

    for i in range(len(answers)):
        if num1OMR[i]==answers[i]:
            num1Count+=1
        if num2OMR[i] == answers[i]:
                num2Count += 1
        if num3OMR[i]==answers[i]:
            num3Count+=1

    temp=[(num1Count,1),(num2Count,2),(num3Count,3)]
    temp.sort(reverse=True)
    maxCount =temp[0][0]
    for i in range(len(temp)):
        if maxCount==temp[i][0]:
            answer.append(temp[i][1])
        else:
            break
    answer.reverse()
    return answer