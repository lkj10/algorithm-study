def solution(absolutes, signs):
    result = 0
    for i, v in enumerate(absolutes):
        if signs[i] == True: result += absolutes[i]
        else: result -= absolutes[i]
            
    return result