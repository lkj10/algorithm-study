class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        List = [1]*len(nums)
        for i in range(len(List)):
            for j in range(i, len(nums)):
                if nums[j] > nums[i]:
                    List[j] = max(List[j], List[i] + 1)
                    
        return max(List)