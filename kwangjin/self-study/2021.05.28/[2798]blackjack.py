import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())

List = list(map(int, input().split()))

MAX = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            SUM = List[i] + List[j] + List[k]
            if M >= SUM and SUM > MAX:
                MAX = SUM

print(MAX)