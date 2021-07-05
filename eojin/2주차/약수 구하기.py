n,m=map(int,input().split())
result=[]

for i in range(1,n+1):
    if n%i==0:
        result.append(i)
if len(result)<m:
    print(0)
else:
    print(result[m-1])

