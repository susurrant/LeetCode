"""
3. Longest Substring Without Repeating Characters
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return  0

        rlen = 1
        for i in range(len(s)-1):
            for j in range(i+rlen, len(s)+1):
                if len(set(s[i:j])) == (j-i):
                    rlen = j-i
                else:
                    break
        return rlen


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring('bbbbbb'))