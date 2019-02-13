"""
14. Longest Common Prefix
"""

class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        if not len(strs):
            return ""

        l = len(strs[0])
        for i in range(l, 0, -1):
            prefix = strs[0][:i]
            tag = True
            for s in strs:
                if not s.startswith(prefix):
                    tag = False
                    break
            if tag:
                return prefix
        return ""

if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["a"]))
