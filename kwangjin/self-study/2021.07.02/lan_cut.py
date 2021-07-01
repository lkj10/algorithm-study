import sys
sys.stdin = open("input.txt", "r")

K, N = map(int, sys.stdin.readline().split())
List = list()
for i in range(K):
    List.append(int(sys.stdin.readline()))

lt = 1
rt = max(List)
cnt = 0
mid = 0
while lt <= rt:
    print(lt, rt, mid)
    cnt = 0
    mid = (lt + rt)//2
    for i in List:
        cnt += i//mid
    if cnt >= N:
        res = mid
        lt = mid + 1
    else:
        rt = mid-1

print(res)

