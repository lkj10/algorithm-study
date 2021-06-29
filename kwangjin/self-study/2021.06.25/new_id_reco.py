import re


def solution(new_id):
    answer = ''
    List = list(new_id)
    temp = list()
    temp2 = list()
    cnt = 0
    # step 1
    for i in range(len(List)):
        if List[i].isalpha():
            List[i] = List[i].lower()

    # step 2
    for i in range(len(List)):
        if List[i].isalpha() or List[i].isdecimal() or List[i] == '-' or List[i] == '_' or List[i] == '.':
            temp.append(List[i])
    # step 3
    for i in temp:
        temp2.append(i)
        if i == '.':
            cnt += 1
            if cnt == 2:
                temp2.pop()
                cnt = 1
        else:
            cnt = 0

    # step 4
    if temp2 and temp2[0] == '.':
        temp2.pop(0)
    if temp2 and temp2[-1] == '.':
        temp2.pop()

    # step 5
    if temp2 == []:
        temp2.append('a')

    # step 6
    if len(temp2) >= 16:
        temp2 = temp2[:15]
        if temp2[-1] == '.':
            temp2.pop()

    # step 7
    if len(temp2) <= 2:
        temp_str = temp2[-1]
        while len(temp2) < 3:
            temp2.append(temp_str)

    return ''.join(temp2)


def solution(new_id):
    #new_id = re.sub('[A-Z]+', lambda m : m.group().lower(), new_id)
    new_id = new_id.lower()
    new_id = re.sub('[^a-z0-9\-_\.]', '', new_id)
    new_id = re.sub('\.+', '.', new_id)
    new_id = re.sub('^\.|\.$', '', new_id)
    new_id = ('a' if len(new_id) == 0 else new_id[:15])
    new_id = re.sub('\.$', '', new_id)
    new_id = new_id + new_id[-1] * \
        (3 - len(new_id)) if len(new_id) < 3 else new_id
    return new_id
