import sys
sys.stdin = open("input.txt", "r")
N = int(input())
cnt = 0
List = [0]*(N)
List[1] = 1
List[2] = 2
List[3] = 1
1 2 3 4 5 6 7 8
1 1 1 2 3 2 3


def f(n):
    if n == 1 or n == 2 or n == 3:
        return List[n]
    else:
        return


for i in range(N+1):
