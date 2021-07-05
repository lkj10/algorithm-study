def solution(s):
    stack=[]
    for i in s:
        if not stack:
            stack.append(i)
            continue
        if stack[-1]==i:
            stack.pop()
        else:
            stack.append(i)

    if not stack:
        return 1
    else: return 0