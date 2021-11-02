import sys

sys.stdin = open("input.txt", "r")

T = int(input())
List = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for i in range(10, 101):
    List.append(List[i-3] + List[i-2])


for _ in range(T):
    N = int(input())
    print(List[N-1])