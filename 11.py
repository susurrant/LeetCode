"""
11. Container With Most Water
"""


class OldSolution:
    def maxArea(self, height: 'List[int]') -> 'int':
        l = len(height)
        a = 0
        for i in range(l-1):
            for j in range(i+1, l):
                ta = (j-i)*min(height[i], height[j])
                if ta > a:
                    a = ta
        return a

class Solution:
    def maxArea(self, height: 'List[int]') -> 'int':
        r = len(height) - 1
        l = 0
        a = 0
        while l < r:
            ta = (r-l)*min(height[l], height[r])
            if ta > a:
                a = ta
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return a


if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))