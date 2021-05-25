import sys

input = sys.stdin.readline


def SameNum(array, idx, n):
    lastValue = array[idx - 1][1]
    value = array[idx][1]
    if lastValue == value:
        return idx + 1
    while idx < n:
        if array[idx][1] == value:
            array[idx][1] = lastValue + 1
        else:
            break
        idx += 1
    return idx


n = int(input())
temp = list(map(int, input().split()))
array = [[i, temp[i]] for i in range(n)]
array.sort(key=lambda x: x[1])
idx = 1
while idx < n:
    idx = SameNum(array, idx, n)

minValue = array[0][1]
array.sort(key=lambda x: x[0])
for i in range(n):
    print(array[i][1] - minValue)
