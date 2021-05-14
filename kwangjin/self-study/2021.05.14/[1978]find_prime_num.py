import sys
from collections import deque
sys.stdin = open("input.txt", "r")

N = int(input())
cnt = 0
List = map(int, input().split())
for i in List:
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            cnt += 1
print(cnt)

######################################
# 조건에서 N개의 수는 1000 이하의 자연수라 했으므로
# 에라토스테네스의 체를 1000개를 만들고 비교해도 된다.
