import math
def solution(n, stations, w):
    coverage = w * 2 + 1
    result = 0
    stations.insert(0, -w)
    stations.append(n + w + 1)
    
    for i in range(0, len(stations) - 1):
        dist = stations[i + 1] - stations[i] - coverage
        if dist > 0: result += math.ceil(dist / coverage)
    
    return result;