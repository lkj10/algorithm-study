import sys
sys.stdin = open("input.txt", "r")


T = int(input())
stack = list()

for _ in range(T):
    N = int(input())
    if N == 0:
        stack.pop()
    else:
        stack.append(N)

print(sum(stack))
