import sys
sys.stdin = open("input.txt", "r")

N = int(input())
M = int(input())
S = input()
cnt = 0
res = 0
stack = []
for i in range(M):
    if S[i] == 'I':
        stack.append(i)
for i in range(1, len(stack)):
    if stack[i] - stack[i-1] == 2:
        cnt += 1
    else:
        cnt = 0
    
    if cnt >= N:
        res += 1

print(res)

