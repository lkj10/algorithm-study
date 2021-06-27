import heapq
import collections

def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]
    
    for u, v, w in road:
        graph[u].append((v, w))
        graph[v].append((u, w))

    # 시작 노드, 소요 시간
    Q = [(1, 0)]
    dist = collections.defaultdict(int)
    
    while Q:
        node, time = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time  + w
                heapq.heappush(Q, (v, alt))
                
    result = 0
    for v in dist.values():
        if v <= K:
            result += 1
            
    return result