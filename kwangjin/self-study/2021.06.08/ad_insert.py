def solution(play_time, adv_time, logs):
    answer = ''

    play_HH, play_MM, play_SS = map(int, play_time.split(':'))
    adv_HH, adv_MM, adv_SS = map(int, adv_time.split(':'))
    adv_SS += adv_HH*3600 + adv_MM * 60
    List = [0] * (play_HH*3600 + play_MM * 60 + play_SS)
    List_MAX = [0] * (play_HH*3600 + play_MM * 60 + play_SS - adv_SS)
    result = 0
    MAX, idx = 0, 0

    for i in logs:
        start_time, end_time = map(str, i.split('-'))
        start_HH, start_MM, start_SS = map(int, start_time.split(':'))
        end_HH, end_MM, end_SS = map(int, end_time.split(':'))
        start_SS += start_HH*3600 + start_MM * 60
        end_SS += end_HH*3600 + end_MM * 60
        #print(start_SS, start_time, end_SS, end_time)
        for j in range(start_SS, end_SS):
            List[j] += 1
        # print(sum(List[start_SS:end_SS]))

    # List_MAX[0] = sum(List[:adv_SS])
    # List_MAX[1] = List_MAX[0] - List[0] + List[adv_SS]
    # List_MAX[2] = List_MAX[1] - List[1] + List[1+adv_SS]
    for i in range(1, len(List) - adv_SS):
        List_MAX[i] = List_MAX[i-1] - List[i-1] + List[adv_SS+i-1]
        if List_MAX[i] > MAX:
            MAX = List_MAX[i]
            idx = i

    if List_MAX:
        result = idx

    result_HH = result // 3600
    result_MM = (result - result_HH*3600) // 60
    result_SS = result - result_HH*3600 - result_MM * 60
    ##print(result_HH, result_MM, result_SS)

    answer = f"{str(result_HH).zfill(2)}:{str(result_MM).zfill(2)}:{str(result_SS).zfill(2)}"
    return answer


print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00",
                                        "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
