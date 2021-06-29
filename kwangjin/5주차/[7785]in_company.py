import sys
sys.stdin = open("input.txt", "r")


T = int(input())
dic = {}
result = []
for _ in range(T):
    temp = list(input().split())
    if temp[1] == "enter":
        dic[temp[0]] = 1
    elif temp[1] == "leave":
        dic[temp[0]] = 0

for idx, val in dic.items():
    if val == 1:
        result.append(idx)

result.sort(reverse=True)

for i in result:
    print(i)
