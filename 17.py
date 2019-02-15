"""
17. Letter Combinations of a Phone Number
"""


class Solution:
    def letterCombinations(self, digits: 'str') -> 'List[str]':
        t = {'2':'abc',
             '3':'def',
             '4':'ghi',
             '5':'jkl',
             '6':'mno',
             '7':'pqrs',
             '8':'tuv',
             '9':'wxyz'}

        r = []

        for d in digits:
            if r:
                tem = []
                for item in r:
                    for c in t[d]:
                        tem.append(item+c)
                r = tem.copy()
            else:
                r = list(t[d])

        return r


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('23'))
