import math

def solution(n, stations, w):
    answer = 0
    station_list = [(0, 0)]
    
    for station in stations:
        if station - w > 0 :
            left = station - w
        else:
            left = 0
        if station + w < n+1 :
            right = station + w
        else:
            right = n+1
        station_list.append((left, right))
    
    station_list.append((n+1, n+1))
    
    for i in range(len(station_list)-1):
        dis = station_list[i+1][0] - station_list[i][1] - 1
        answer += math.ceil(dis/(2*w + 1))

    return answer