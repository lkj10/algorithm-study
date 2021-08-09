def solution(s):
    answer = ''
    num_dic = { 'zero' : 0, 'one' : 1,  'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9}
    temp_str = ''
    for i in s:
        if i.isdecimal():
            answer += i
        else:
            temp_str += i
            if temp_str in num_dic.keys():
                answer += str(num_dic[temp_str])
                temp_str = ''
        
    return int(answer)