def solution(x):
    temp = x
    SUM = 0
    while(x > 0):
        SUM += x % 10
        x = x//10

    if temp % SUM == 0:
        return True

    return False
