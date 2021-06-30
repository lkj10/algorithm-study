import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
List_1 = list()
List_2 = list()
for i in range(N):
    List_1.append(input())

for i in range(M):
    List_2.append(input())

result = set(List_1) & set(List_2)
print(len(result))
for i in sorted(result):
    print(i)