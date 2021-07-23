def solution(routes):
    routes.sort()
    temp = routes[0][1]
    routes.pop(0)
    answer = 1
    for route in routes:
        if route[0] <= temp:
            temp = min(route[1],temp)
        else:
            temp = route[1]
            answer += 1
    return answer