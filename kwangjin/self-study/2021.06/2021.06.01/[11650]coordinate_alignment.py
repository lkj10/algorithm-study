import sys
sys.stdin = open("input.txt", "r")

T = int(input())

List = list()

for _ in range(T):
    M, N = map(int, input().split())
    List.append((M, N))

List.sort(key = lambda x : (x[0], x[1]))

for i in List:
    print(i[0], i[1])