class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        idx = -1
        for i in range(size-1,0,-1):
            if nums[i] > nums[i-1]:
                idx = i-1
                break
        if idx == -1:
            nums.reverse()
        else:
            big = -1
            for i in range(idx+1, size):
                if nums[i] > nums[idx]:
                    if big == -1 or nums[big] > nums[i]:
                        big = i
            nums[idx], nums[big] = nums[big], nums[idx]
            nums[idx+1:]= sorted(nums[idx+1:])


s = Solution()
a = [1,2,6,5,4]
s.nextPermutation(a)
print(a)