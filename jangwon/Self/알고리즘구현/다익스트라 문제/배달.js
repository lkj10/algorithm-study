// 프로그래머스 배달
// 다익스트라로 해결
function solution(N, road, K) {
    const visited = Array.from({length: N + 1}, () => Infinity);
    const graph = Array.from({length: N + 1}, () => Array());
    let result = 0;
    
    // 그래프 구성
    for (const [u, v, w] of road) {
        graph[u].push([v, w]);
        graph[v].push([u, w]);
    }
    
    // 시작 노드, 배달 시간
    let Q = [[1, 0]];
    visited[1] = 0;
    
    while (Q.length) {
        const [node, time] = Q.shift();
        
        for (let i = 0; i < graph[node].length; i++) {
            // 최소 값 갱신
            const next = graph[node][i];
            if (visited[next[0]] > visited[node] + next[1]) {
                visited[next[0]] = visited[node] + next[1];
                Q.push(next);
            }
        }
    }
    
    visited.forEach((v) => (v <= K ? result += 1 : false));
    return result;
}