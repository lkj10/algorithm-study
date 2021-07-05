import sys
sys.stdin = open("input.txt", "r")


# sys.setrecursionlimit(10000)

# N, K = map(int, input().split())
# List = []
# visit = [0] * K
# MAX = 0
# IMP = 0
# result = 0


# def DFS(L, SUM, IMP):
#     global MAX
#     print(SUM, IMP)
#     if IMP > N:
#         return
#     if SUM > MAX:
#         MAX = SUM

#     for i in range(len(List)):
#         if visit[i] == 0:
#             visit[i] = 1
#             DFS(L+1, SUM+List[i][0], IMP+List[i][1])
#             visit[i] = 0


# for _ in range(K):
#     I, T = map(int, input().split())
#     List.append((I, T))
# DFS(0, 0, 0)
# print(MAX)

M, N = map(int , sys.stdin.readline().split())
List = [0] * (M+1)
for i in range(N):
    A, B = map(int , sys.stdin.readline().split())
    for j in range(M, B-1, -1):
        List[j] = max(List[j], List[j-B] + A)
print(List[M])




