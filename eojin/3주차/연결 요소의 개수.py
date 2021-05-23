from collections import Counter
def FindParent(parent, x):
    if parent[x] != x:
        parent[x] = FindParent(parent, parent[x])
    return parent[x]


def UnionParent(parent, a, b):
    a = FindParent(parent, a)
    b = FindParent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n, m = map(int, input().split())
parent = [x for x in range(n + 1)]
for i in range(m):
    a,b = map(int,input().split())
    UnionParent(parent,a,b)
for i in range(1,n+1):
    FindParent(parent,i)

print(len(Counter(parent[1:])))