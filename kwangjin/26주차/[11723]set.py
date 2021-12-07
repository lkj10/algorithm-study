import sys
sys.stdin = open("input.txt", "r")

M = int(input())

List = [0]*21

for _ in range(M):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == "add":
        num = int(cmd[1])
        List[num] = 1

    if cmd[0] == "remove":
        num = int(cmd[1])
        List[num] = 0

    if cmd[0] == "check":
        num = int(cmd[1])
        print(List[num])

    if cmd[0] == "toggle":
        num = int(cmd[1])
        if List[num] == 1 :
            List[num] = 0
        else:
            List[num] = 1

    if cmd[0] == "all":
        List = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    if cmd[0] == "empty":
        List = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    
