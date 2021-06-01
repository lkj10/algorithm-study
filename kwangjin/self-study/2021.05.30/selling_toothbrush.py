def solution(enroll, referral, seller, amount):

    answer = [0]*len(enroll)
    dic = {}

    def DFS(seller, amount):
        amount_01 = int(amount * 0.1)
        amount_09 = amount - amount_01
        if seller[0] == "-":
            pass
        else:
            idx = dic[seller][0]
            if amount < 10:
                answer[idx] += amount
            else:
                answer[idx] += amount_09
                DFS(dic[seller][1], amount_01)

    for i in range(len(enroll)):
        dic[enroll[i]] = [i]

    for i in range(len(referral)):
        dic[enroll[i]].append(referral[i])

    for i in range(len(seller)):
        DFS(seller[i], amount[i]*100)

    return answer
