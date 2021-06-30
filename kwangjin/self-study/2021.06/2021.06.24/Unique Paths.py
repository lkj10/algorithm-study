class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        List = [[0]*(n+1) for i in range(m+1)]
        List[1][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == 1 and j == 1:
                    continue
                List[i][j] = List[i-1][j] + List[i][j-1]
        
        return List[m][n]
            