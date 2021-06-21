def solution(m, musicinfos):

    answer = "(None)"
    my_list = list()
    MAX = 0
    for i in m:
        if i == "#":
            temp = my_list.pop() + '#'
            my_list.append(temp)
        else:
            my_list.append(i)

    for i in musicinfos:
        song_list = list()
        temp = ''
        time_start, time_end, title, song = map(str, i.split(","))
        time_start_hour, time_start_min = map(int, time_start.split(':'))
        time_end_hour, time_end_min = map(int, time_end.split(':'))
        time = (time_end_hour - time_start_hour) * \
            60 + (time_end_min - time_start_min)

        for i in song:
            if i == "#":
                temp = song_list.pop() + '#'
                song_list.append(temp)
            else:
                song_list.append(i)

        if time > len(song_list):
            song_list = (time//len(song_list))*song_list + \
                song_list[:time % len(song_list)]
        elif len(song_list) > time:
            song_list = song_list[:time]

        k = 0

        for i in song_list:

            if i == my_list[k]:
                k += 1
            else:
                k = 0
                if i == my_list[k]:
                    k += 1

            if k == len(my_list):
                if time > MAX:
                    MAX = time
                    answer = title
                break

    return answer
