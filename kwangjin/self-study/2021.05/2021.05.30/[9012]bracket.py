import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for _ in range(T):
    stack = []
    List = list(input())
    for i in List:
        if i == "(":
            stack.append(i)
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                print("NO")
                break
    else:
        if stack:
            print("NO")
        else:
            print("YES")
