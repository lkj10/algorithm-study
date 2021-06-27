INF=int(1e9)
def solution(n,relation):
    answer=[0]*(n+1)
    graph=[[INF]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        graph[i][i]=0
    for a,b in relation:
        graph[a][b]=1
        graph[b][a]=1

    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

    for row in range(1,n+1):
        count=0
        for x in range(1,n+1):
            if graph[row][x]==1 or graph[row][x]==2:
                count+=1
        answer[row]=count
    return answer[1:]

print(solution(5,[[1,2],[4,2],[3,1],[4,5]]))
print(solution(7,[[1,2],[4,2],[3,1],[4,5],[6,7]]))