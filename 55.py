class Solution:
    def canJump(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            flag = False
            for j in range(i - 1, -1, -1):
                if nums[j] + j >= i:
                    flag = True
                    break
            if not flag:
                return False
        return True


s = Solution()
print(s.canJump([2,3,1,1,4]))