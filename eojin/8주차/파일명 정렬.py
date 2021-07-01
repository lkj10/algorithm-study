def FileSort(f):
    head = ""
    number = ""
    headCheck = False
    numCheck = False
    for x in range(len(f)):
        if not f[x].isdigit() and numCheck == False:
            headCheck = True
            head += f[x]
        elif f[x].isdigit():
            numCheck = True
            number += f[x]
        elif not f[x].isdigit() and numCheck == True:
            break
    return (head.lower(), int(number))


def solution(files):
    answer = []
    files.sort(key=FileSort)
    return files


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
