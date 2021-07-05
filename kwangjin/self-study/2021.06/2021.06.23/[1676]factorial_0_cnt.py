import sys
sys.stdin = open("input.txt", "r")

N = int(input())
M = 1
cnt = 0

for i in range(1, N+1):
    M *= i
for i in range(len(str(M))-1, -1, -1):
    if str(M)[i] != '0':
        break
    cnt += 1
print(cnt)
