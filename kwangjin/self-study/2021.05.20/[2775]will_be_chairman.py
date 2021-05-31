import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for _ in range(T):
    K = int(input())
    N = int(input())
    List = [i for i in range(1, N+2)]

    for i in range(K):
        for j in range(1, N+1):
            List[j] += List[j-1]
    print(List[N-1])



