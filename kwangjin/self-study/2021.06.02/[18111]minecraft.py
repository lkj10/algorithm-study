import sys
sys.stdin = open("input.txt", "r")

N, M, B = map(int, sys.stdin.readline().split())

List = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = 21470000000
height = 0
for i in range(257):
    max = 0
    min = 0
    for j in range(N):
        for k in range(M):
            if List[j][k] > i:
                max += (List[j][k] - i)
            else:
                min += (i - List[j][k])
    inven = max + B
    if inven < min:
        continue
    time = 2*max + min

    if ans >= time:
        ans = time
        height = i

print(ans, height)
