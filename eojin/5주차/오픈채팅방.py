def solution(record):
    uids = {}
    for i in record[::-1]:
        temp = i.split()
        if temp[0] == "Leave":
            continue

        if not uids.get(temp[1]):
            uids[temp[1]] = temp[2]

    answer = []
    for i in record:
        temp = i.split()

        if temp[0] == "Leave":
            answer.append("{0}님이 나갔습니다.".format(uids[temp[1]]))

        elif temp[0] == "Enter":
            answer.append("{0}님이 들어왔습니다.".format(uids[temp[1]]))

    return answer