from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited=[[0]*m for i in range(n+1)]
    q=deque([])
    q.append((0,0))
    visited[0][0]=1

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<m and maps[nx][ny]==1:
                if visited[nx][ny]==1:
                    continue
                maps[nx][ny]=maps[x][y]+1
                visited[nx][ny]=1
                q.append((nx,ny))
    if maps[n-1][m-1]==1:
        return -1
    return maps[n-1][m-1]