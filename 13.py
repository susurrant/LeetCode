"""
13. Roman to Integer
"""

class Solution:
    def romanToInt(self, s: 'str') -> 'int':
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        r = d[s[0]]
        for i in range(1, len(s)):
            if d[s[i-1]] < d[s[i]]:
                r -= 2*d[s[i-1]]
            r += d[s[i]]

        return r

if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('MCMXCIV'))