"""
9. Palindrome Number
"""

class Solution:
    def isPalindrome(self, x: 'int') -> 'bool':
        if x < 0:
            return False

        s1 = str(x)
        s2 = s1[::-1]
        if s1 == s2:
            return True
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(1221))