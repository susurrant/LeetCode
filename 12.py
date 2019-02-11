"""
12. Integer to Roman
"""

class Solution:
    def intToRoman(self, num: 'int') -> 'str':
        r = ''
        g = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        s = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        b = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        q = ['', 'M', 'MM', 'MMM']
        l = [g, s, b, q]
        i = 0
        while num:
            d = num % 10
            r = l[i][d] + r
            i += 1
            num = num // 10
        return r.strip()

if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(3000))
