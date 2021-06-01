def solution(numbers, hand):
    answer = ''
    phone_L = [1, 4, 7]
    phone_R = [3, 6, 9]
    phone_MID = [2, 5, 8, 0]
    
    L_now_x, L_now_y = 3, 0 
    R_now_x, R_now_y = 3, 2
    MID_now_x, MID_now_y = 0, 0
    L_dis, R_dis = 0, 0
    
    for i in numbers:
        if i in phone_L:
            answer += "L"
            L_now_x, L_now_y = phone_L.index(i), 0
        elif i in phone_R:
            answer += "R"
            R_now_x, R_now_y = phone_R.index(i), 2
        else:
            MID_now_x, MID_now_y = phone_MID.index(i), 1
            L_dis = abs(L_now_x - MID_now_x) + abs(L_now_y - MID_now_y)
            R_dis = abs(R_now_x - MID_now_x) + abs(R_now_y - MID_now_y)
            if L_dis > R_dis:
                answer += "R"
                R_now_x, R_now_y = MID_now_x, MID_now_y
            elif R_dis > L_dis:
                answer += "L"
                L_now_x, L_now_y = MID_now_x, MID_now_y
            else:
                if hand == "right":
                    answer += "R"
                    R_now_x, R_now_y = MID_now_x, MID_now_y
                elif hand == "left":
                    answer += "L"
                    L_now_x, L_now_y = MID_now_x, MID_now_y
                    
    return answer