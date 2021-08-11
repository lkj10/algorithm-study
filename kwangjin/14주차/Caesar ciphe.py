def solution(s, n):
    answer = ''

    for i in s:
        if i == ' ':
            answer += i
        else:
            temp = ord(i) + n
            if ord('A') <= ord(i) <= ord('Z'):
                if temp > ord('Z'):
                    temp -= 26
            elif ord('a') <= ord(i) <= ord('z'):
                temp = ord(i) + n
                if temp > ord('z'):
                    temp -= 26
            answer += chr(temp)

    return answer
