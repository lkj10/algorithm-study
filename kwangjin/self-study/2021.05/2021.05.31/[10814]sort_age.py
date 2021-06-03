import sys
sys.stdin = open("input.txt", "r")

T = int(input())
List = []
for i in range(T):
    M, N = map(str, input().split())
    List.append((i, int(M), N))

List = sorted(List, key=lambda x: (x[1], x[0]))

for i in List:
    print(i[1], i[2])
