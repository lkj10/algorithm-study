def solution(nums):
    dp = [1] * len(nums)

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i]=max(dp[i],dp[j]+1)

    return max(dp)

print(solution([0,1,0,3,2,3]))