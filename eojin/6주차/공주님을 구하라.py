import sys
from collections import deque
#sys.stdin = open("input.txt","r")
dx=[-1,0,1,0]
dy=[0,1,0,-1]
INF=int(1e9)
def no_gram():
    visited[0][0]=0
    q=deque([(0,0)])
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny < m:
                if visited[nx][ny]==-1 and array[nx][ny]!=1:
                    visited[nx][ny]=visited[x][y]+1
                    q.append((nx,ny))
    if visited[n-1][m-1]==-1:
        return INF
    else:
        return visited[n-1][m-1]

def gram():
    gram_pos=(0,0)
    gram_check=False
    if array[0][0]!=2:
        visited[0][0] = 0
        q = deque([(0, 0)])
        while q:
            x, y = q.popleft()
            if array[x][y]==2:
                gram_pos=(x,y)
                gram_check=True
                break
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= 0 and nx < n and ny >= 0 and ny < m:
                    if visited[nx][ny] == -1 and array[nx][ny] != 1:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))
    if gram_check:
        return visited[gram_pos[0]][gram_pos[1]] + abs(gram_pos[0] - (n - 1)) + abs(gram_pos[1] - (m - 1))
    else:
        return INF


n,m,t=map(int,input().split())
array=[list(map(int,input().split())) for _ in range(n)]
visited=[[-1] * m for _ in range(n)]
result1 =no_gram()
visited=[[-1] * m for _ in range(n)]
result2 = gram()
result =min(result1,result2)
if result==INF or result>t:
    print("Fail")
else:
    print(result)
