"""
18. 4Sum
"""

import collections

class Solution:
    def fourSum(self, nums: 'List[int]', target: int) -> 'List[List[int]]':
        nums.sort()
        if len(nums) < 4 or 4 * nums[0] > target or 4 * nums[-1] < target: return []
        total_map = collections.defaultdict(list)
        results = set()

        for idx1 in range(len(nums) - 1):
            for idx2 in range(idx1 + 1, len(nums)):
                diff = target - nums[idx1] - nums[idx2]
                total_map[diff].append((idx1, idx2))

        for idx1 in range(len(nums) - 3):
            for idx2 in range(idx1 + 1, len(nums)):
                total = nums[idx1] + nums[idx2]
                if total in total_map:
                    for pair in total_map[total]:
                        if pair[0] > idx2:
                            results.add((nums[idx1], nums[idx2], nums[pair[0]], nums[pair[1]]))

        return [list(result) for result in results]



if __name__ == '__main__':
    s = Solution()
    print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
