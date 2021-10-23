import sys
sys.stdin = open("input.txt", "r")

N = int(input())
List = list(map(int, input().split()))
B, C = map(int, input().split())
res = 0
for i in range(N):
    SUM = List[i]
    SUM -= B
    res += 1
    if SUM <= 0 :
        continue
    
    if SUM % C == 0 :
        res += SUM//C
    else :
        res += SUM//C + 1

print(res)