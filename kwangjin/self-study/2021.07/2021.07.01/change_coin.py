import sys
sys.stdin = open("input.txt", 'r')
N = int(sys.stdin.readline())
List = list(map(int, sys.stdin.readline().split()))
List.sort(reverse=True)
M = int(sys.stdin.readline())
dy = [1000]*(M+1)
dy[0] = 0

for i in List:
    for j in range(i, M+1):
        dy[j] = min(dy[j], dy[j-i]+1)

print(dy)