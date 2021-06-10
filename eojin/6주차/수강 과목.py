import sys

sys.stdin = open("input.txt", 'r')
n,k=map(int,input().split())
dp=[[0]*(n+1) for i in range(k+1)]
array=[[0,0]]

for _ in range(k):
    array.append(list(map(int,input().split())))
for i in range(1,k+1):
    importance=array[i][0]
    study_time=array[i][1]
    for j in range(1,n+1):
        if j<study_time:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-study_time]+importance)
print(dp[k][n])
