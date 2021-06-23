def BalancedString(p):
    count = 0
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        else:
            count -= 1

        if count == 0:
            return p[:i + 1], p[i + 1:]


def CollectString(p):
    count = 0
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        else:
            count -= 1

        if count < 0:
            return False
    return True


def ReverseString(p):
    answer = ""
    for i in p:
        if i == "(":
            answer += ")"
        else:
            answer += "("
    return answer


def solution(p):
    answer = ''
    if len(p) == 0:
        return ""

    u, v = BalancedString(p)
    if CollectString(u):
        answer += u + solution(v)
    else:
        answer = "(" + solution(v) + ")" + ReverseString(u[1:-1])

    return answer


print(solution("(()())()"))
