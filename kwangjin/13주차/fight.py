def solution(n,a,b):
    answer = 1
    r_A = (a+1)//2
    r_B = (b+1)//2
    while r_A != r_B :
        r_A = (r_A+1)//2
        r_B = (r_B+1)//2
        answer+=1

    return answer