import sys
sys.stdin = open("input.txt", "r")

N, K = map(int, input().split())

List = list()

for _ in range(N):
    List.append(int(input()))

res = 0
for i in range(N-1, -1, -1):
    if List[i] <= K:
        res += K//List[i]
        K = K - List[i] * (K//List[i])
        if K <= 0 : 
            break
    
print(res)