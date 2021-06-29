import sys
sys.stdin = open("input.txt", "r")


N_int = int(input())
List = [0] * 10
M = int(input())
if M > 0:
    M_temp = list(map(int, input().split()))
    for i in range(M):
        List[M_temp[i]] = 1

now = 100

cnt = abs(now - N_int)

for num in range(1000001):
    num = str(num)
    for i in range(len(num)):
        if List[int(num[i])] == 1:
            break
        elif i == len(num) - 1:
            cnt = min(cnt, abs(N_int - int(num)) + len(num))

print(cnt)
