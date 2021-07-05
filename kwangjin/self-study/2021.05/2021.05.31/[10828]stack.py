import sys
sys.stdin = open("input.txt", "r")

T = int(sys.stdin.readline())

stack = list()

for _ in range(T):
    M = list(sys.stdin.readline().split())
    if M[0] == "push" :
        stack.append(int(M[1]))
    elif M[0] == "top" :
        print(stack[-1] if stack else -1)
    elif M[0] == "pop" :
        print(stack.pop() if stack else -1)
    elif M[0] == "size":
        print(len(stack) if stack else 0)
    elif M[0] == "empty":
        print(0 if stack else 1)

