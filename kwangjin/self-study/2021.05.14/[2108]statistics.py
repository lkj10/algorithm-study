import sys
sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
List = list()
for _ in range(N):
    List.append(int(sys.stdin.readline()))
List.sort()

print(int(sum(List)/N+0.5) if sum(List) > 0 else int(sum(List)/N - 0.5))
print(List[N//2])

MAX = 0
cnt = 1
temp = 4001
temp_list = list()
for i in List:
    if i == temp:
        cnt += 1
    else:
        cnt = 1
    if cnt >= MAX:
        MAX = cnt
        temp_list.append((MAX, i))
    temp = i
temp_list.sort(key=lambda x: (-x[0], x[1]))
if len(temp_list) > 1 and temp_list[0][0] == temp_list[1][0]:
    print(temp_list[1][1])
else:
    print(temp_list[0][1])

print(List[-1] - List[0])
