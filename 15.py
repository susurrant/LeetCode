"""
15. 3Sum
"""


class OldSolution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        l = len(nums)
        r = []
        for i in range(l-2):
            for j in range(i+1, l-1):
                if -nums[i]-nums[j] in nums[j+1:]:
                    t = sorted([nums[i], nums[j], -nums[i]-nums[j]])
                    tag = True
                    for s in r:
                        if t[0] == s[0] and t[1] == s[1] and t[2] == s[2]:
                            tag = False
                            break
                    if tag:
                        r.append(t)
        return r

class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        res = []
        nums.sort()
        length = len(nums)
        for i in range(length - 2):
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i - 1]: continue

            l, r = i + 1, length - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4, 0, 0]))
