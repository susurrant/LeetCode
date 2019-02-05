"""
7. Reverse Integer
"""


class Solution:
    def reverse(self, x: 'int') -> 'int':
        if x == 0:
            return 0

        tag = False
        if x < 0:
            tag = True
            s = str(x)[:0:-1]
        else:
            s = str(x)[::-1]

        i = 0
        while True:
            if s[i] == '0':
                i += 1
            else:
                break

        if tag:
            r = -1 * int(s[i:])
        else:
            r = int(s[i:])

        if r < -2 ** 31 or r > 2 ** 31 - 1:
            return 0
        else:
            return r


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(0))