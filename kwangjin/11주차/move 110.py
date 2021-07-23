def solution(s):
    answer = []
    for s_ in s:
        stack = []
        temp = ''
        for s__ in s_: 
            if s__ == "0" and len(stack) > 1 and stack[-1] == stack[-2] == "1":
                temp += stack.pop()
                temp += stack.pop()
                temp += s__
            else:
                stack.append(s__)
        for i in range(len(stack)-1, -1, -1):
            if stack[i] == '0':
                answer.append(''.join(stack[:i+1])+temp+''.join(stack[i+1:]))
                break
        else:
            answer.append(temp+''.join(stack))
    return answer