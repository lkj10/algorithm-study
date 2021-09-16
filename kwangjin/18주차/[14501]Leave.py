import sys
sys.stdin = open("input.txt", "r")

N = int(input())
List = [0]*30
for day in range(1, N+1):
    T, P = map(int, input().split())
    List[day] = max(List[day], List[day-1])
    List[day + T] =  max(List[day+T], List[day] + P)
List[N+1] = max(List[N+1], List[N])
print(List[N+1])