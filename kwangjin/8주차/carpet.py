def solution(brown, yellow):

    List = list()

    for i in range(1, yellow+1):
        if yellow % i == 0:
            List.append(i)

    for i in range(len(List)//2 + 1):
        B, A = List[i], List[-1-i]
        if brown == A*2 + B*2 + 4:
            return [A+2, B+2]
