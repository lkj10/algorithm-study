

def is_pallindrome(string,start,end):

    if start!=end and string[start]!=string[end]:
        return ""
    start-=1
    end+=1


    while start>=0 and end < len(string):
        if string[start] == string[end]:
            start-=1
            end+=1
        else:
            start+=1
            end-=1
            break

    if start==-1 or len(string)==end:
        start+=1
        end-=1
    return string[start:end+1]

def solution(s):
    answer = ""

    if not s or len(s)==1 or s==s[::-1]:
        return len(s)

    for i in range(0,len(s)-1):
        answer=max(is_pallindrome(s,i,i),is_pallindrome(s,i,i+1),answer,key=len)

    return len(answer)

print(solution("bbaa"))
# print(solution("abcdcba"))
# print(solution("abacde"))
# print(solution('abcde'))
# print(solution("a"))
# print(solution("ecdabbcadc"))
# print(solution("ABCCBA"))
# print(solution(""))