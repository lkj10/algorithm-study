def solution(m, musicinfos):
    answer = [0, ""]
    music_dic = dict()
    m=m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")

    for music in musicinfos:
        st, ed, title, sheet = music.split(",")
        sheet = sheet.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
        start = [int(time) for time in st.split(':')]
        end = [int(time) for time in ed.split(':')]
        all_time = (end[0] - start[0]) * 60 + (end[1] - start[1])
        sheet = sheet * (all_time // len(sheet)+1)# + sheet[0:all_time % len(sheet)]
        music_dic[title] = sheet
        if m in sheet:
            if answer[0]<len(sheet):
                answer[0]=len(sheet)
                answer[1]=title
    if answer[0]!=0:
        return answer[1]
    else:
        return "(None)"