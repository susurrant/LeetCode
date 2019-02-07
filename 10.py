"""
10. Regular Expression Matching
"""


class Solution:
    def isMatch(self, s: 'str', p: 'str') -> 'bool':
        idx = 0
        pre_c = s[0]
        for c in p:
            if c == '.':
                idx += 1
                pre_c = ''
            elif c == '*':

            elif c.isalpha():
                if s[idx] == c:
                    idx += 1
                    continue
                else:
                    return False