import sys
sys.stdin = open("input.txt", "r")

while True:
    STR = str(input())
    stack = list()
    if STR == '.':
        break
    for i in STR:
        if i == "[":
            stack.append(i)
        elif i == "(":
            stack.append(i)
        elif i == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                print("no")
                break
        elif i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                print("no")
                break
    else:
        if stack:
            print("no")
        else:
            print("yes")

