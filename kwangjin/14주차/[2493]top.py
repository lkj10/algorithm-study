import sys
sys.stdin = open("input.txt", "r")

T = int(input())
arr = list(map(int, input().split()))

stack = []
answer = [0]*T

for i in range(T-1, -1, -1):
    while stack and arr[i] > stack[-1][0]:
        answer[stack[-1][1]] = i+1
        stack.pop()

    stack.append((arr[i], i))

while stack:
    answer[stack[-1][1]] = 0
    stack.pop()

for i in range(T):
    print(answer[i], end=' ')
