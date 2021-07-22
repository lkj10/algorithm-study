class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        List = [1000] * (amount+1)
        List[0] = 0
        for j in coins:
            for i in range(j,  amount+1):
                List[i] = min(List[i], List[i-j] + 1)
        if List[-1] == 1000:
            return -1
        else:
            return List[-1]