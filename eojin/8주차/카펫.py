import math


def solution(brown, yellow):
    answer = []
    num = brown + yellow
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            if i > num // i:
                col = num // i
                row = i
            else:
                row = num // i
                col = i
            if brown == (row + col) * 2 - 4:
                return [row, col]


print(solution(10, 2))