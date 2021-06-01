import sys
sys.stdin = open("input.txt", "r")

T = int(input())
List = list()

for i in range(T):
    M, N = map(int, input().split())
    List.append((M, N))

for i in range(T):
    rank = 1
    for j in range(T):
        if List[i][0] < List[j][0] and List[i][1] < List[j][1]:
            rank += 1

    print(rank, end=' ')



