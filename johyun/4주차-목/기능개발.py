
def solution(progresses, speeds):
    answer = []
    gap = [0]*len(speeds)
    # speeds2 = np.array(speeds)
    days = []
    for idx, prg in enumerate(progresses):
        gap[idx] = 100 - prg
    for i in range(len(speeds)):
        if gap[i] % speeds[i] != 0:
            days.append(gap[i] // speeds[i] + 1)  # days가 빈리스트인데 인덱스로 넣어주려 해서 오류남. append로!
        else:
            days.append(gap[i] // speeds[i])  # days 완성
    print(days)

    distribute = []
    i=0
    while days:#3
        i = 0
        if len(days)==1:
            distribute.append(1)
            break
        if days[0]>= days[1]:
            days.pop(0)
            i+=1

        else:
            distribute.append(i)
        # else:
        #     days_sl = days[:i+1]
        #     days=days[i+1:]
        #     distribute.append(len(days_sl))
    return distribute

solution([93, 30, 55], [1, 30, 5])
