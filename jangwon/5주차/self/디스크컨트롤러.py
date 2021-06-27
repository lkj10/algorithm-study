def solution(jobs):
    answer = 0
    start = 0 # 현재까지 진행된 작업시간
    length = len(jobs)
    
    jobs = sorted(jobs, key = lambda x : x[1]) # 소요시간 우선 정렬
    print(jobs)
    
    while len(jobs) != 0:
        for i in range(len(jobs)):
            # 대기시간이 현재 진행 시간 보다 적은 경우
            # 작업 진행이 가능하다
            if jobs[i][0] <= start:
                start += jobs[i][1]
                # 현재까지 진행된 시간에서 대기시간을 빼서 더해준다.
                answer += start - jobs[i][0]
                jobs.pop(i)
                break
            # 해당 시점에 아직 작업이 들어오지 않았을 경우
            if i == len(jobs) - 1:
                start += 1
    
    return answer // length