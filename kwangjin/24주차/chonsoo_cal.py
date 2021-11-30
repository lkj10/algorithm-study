import sys

sys.stdin = open("input.txt", "r")

n = int(input())
List = [0]
num1, num2 = map(int, input().split())

m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    List[y] = x

print(List)