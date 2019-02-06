"""
8. String to Integer (atoi)
"""


class Solution:
    def myAtoi(self, str: 'str') -> 'int':
        r = ''
        for x in str:
            if x.isdigit():
                r += x
            elif x in ['+', '-']:
                if not r:
                    r += x
                else:
                    break
            elif x == ' ':
                if not r:
                    continue
                else:
                    break
            else:
                break


        if r in ['', '+', '-']:
            return 0

        i = int(r)
        if i < -2**31:
            return -2**31
        elif i > 2**31-1:
            return 2**31-1

        return i


if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi("3+45"))

