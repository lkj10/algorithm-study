import sys
sys.stdin = open("input.txt", "r")

M, N = map(int, input().split())
# for i in range(M, N+1):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i)

# 위의 식으로 진행을 하면 시간이 너무 오래걸려 문제를 풀지 못한다.

# 에라토스테네스의 체로 소수를 구한다.

List = [1] * (N+1)
result = []
for k in range(2, N+1):
    result.append(k if List[k] == 1 else 0)
    for j in range(k*2, N+1, k):
        List[j] = 0
for i in result:
    if N >= i >= M:
        print(i)
