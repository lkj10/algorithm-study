def solution(play_time, adv_time, logs):
    answer = ''
    logs_List = list()
    
    play_HH, play_MM, play_SS = map(int, play_time.split(':'))
    play_time_List = [0, play_HH*3600+play_MM*60+play_SS]
    logs_List = list([play_time_List])
    
    adv_HH, adv_MM, adv_SS = map(int, adv_time.split(':'))
    adv_time_List = [0, adv_HH*3600+adv_MM*60+adv_SS]
    
    MAX = 0
    
    
    for i in logs:
        start_time , end_time = map(str, i.split('-'))
        start_HH, start_MM, start_SS = map(int, start_time.split(':'))
        end_HH, end_MM, end_SS = map(int, end_time.split(':'))
        logs_List.append([start_HH*3600+start_MM*60+start_SS, end_HH*3600+end_MM*60+end_SS])
        
    for i in range(len(logs_List)):
        #두가지 경우로 나눈다. 1. end_time에서 플레이 시간을 뺀거 2. start_time에서 더한거. 그걸 temp_start, temp_end로 변수를 지정.
        #case 1
        temp_start = logs_List[i][0]
        temp_end = adv_time_List[1] + temp_start
        SUM_start = 0
        for j in range(len(logs_List)):
            if temp_end >= logs_List[j][0] >= temp_start: # logs_start 가 adv_time 안에 있을 경우
                if temp_end >= logs_List[j][1]: # adv_time보다 작을 경우
                    SUM_start += logs_List[j][1] - logs_List[j][0]
                elif logs_List[j][1] > temp_end :#adv_time보다 클 경우
                    SUM_start += temp_end - logs_List[j][0]
                    
            elif temp_start >= logs_List[j][0] and temp_end >= logs_List[j][1]: # log_start는 밖에 있지만 log_end가 안에 있을 경우
                SUM_start += temp_end - temp_start
                
            elif temp_start >= logs_List[j][0] and logs_List[j][1] >= temp_end : #log_List가 adv_time을 감싸고 있을 경우
                SUM_start += temp_start - temp_end
                
        print(SUM_start)
                

    # print(logs_List)
    # print(play_time_List)
    # print(adv_time_List)
    return answer
