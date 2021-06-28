def solution(str1, str2):
    list_str1 = []
    list_str2 = []

    for i in range(len(str1) - 1):
        if str1[i:i + 2].isalpha():
            list_str1.append(str1[i:i + 2].lower())

    for i in range(len(str2) - 1):
        if str2[i:i + 2].isalpha():
            list_str2.append(str2[i:i + 2].lower())

    # Intersection 두 단어 문자간 교집합
    Intersection = []

    # list_str2 차집합 만들기
    if len(list_str1) > len(list_str2):
        for i in list_str1:
            if i in list_str2:
                list_str2.remove(i)
                Intersection.append(i)

    else:
        for i in list_str2:
            if i in list_str1:
                list_str1.remove(i)
                Intersection.append(i)

    # print(list_str1)
    # print(list_str2)
    if len(list_str1 + list_str2) == 0:
        return 65536
    return int(len(Intersection) / len(list_str1 + list_str2) * 65536)