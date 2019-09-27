class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        r = dp[0]
        for i in range(1, n):
            dp[i] = dp[i-1] + nums[i] if dp[i-1] + nums[i] > nums[i] else nums[i]
            r = dp[i] if dp[i] > r else r
        return r

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))