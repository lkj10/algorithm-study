import sys
sys.stdin = open("input.txt", "r")

List = list()
for i in range(1, 10001):
    temp = i + sum(map(int, str(i)))
    List.append(temp)

for j in range(1, 10001):
    if j not in List:
        print(j)
