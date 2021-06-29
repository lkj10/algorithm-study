import sys
sys.stdin = open("input.txt", "r")
N = int(input())
List = [0]*(N+1)
List[1] = 0
for i in range(2, N+1):
    if i % 6 == 0:
        List[i] = min(List[i//2], List[i//3], List[i-1]) + 1
    elif i % 3 == 0:
        List[i] = min(List[i//3], List[i-1]) + 1
    elif i % 2 == 0:
        List[i] = min(List[i//2], List[i-1]) + 1
    else:
        List[i] = List[i-1] + 1

print(List[N])
