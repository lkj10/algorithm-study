def solution(s):
#     List = list(s.split())
#     res = ""
#     for i in List:
#         i = i.lower()
#         res += i[0].upper() + i[1:] + " "
        
#     return res[:-1]

    idx = 0
    res = ""
    for i in s:
        if i == " ":
            idx = 0
            res += i
        else:
            if idx == 0 and i.isalpha(): 
                res += i.upper()
            else:
                res += i.lower()
            idx += 1
    return res