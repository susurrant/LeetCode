class Solution:
    def largestRectangleArea(self, heights) -> int:
        n = len(heights)
        r = 0
        for i in range(n):
            if heights[i]:
                left = right = i
                while left >= 0 and heights[left]>=heights[i]:
                    left -= 1
                while right < n and heights[right]>=heights[i]:
                    right += 1

                a = (right-left-1)*heights[i]
                if a > r:
                    r = a
        return r

s = Solution()
print(s.largestRectangleArea([2,1,5,6,2,3]))