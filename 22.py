class Solution:
    def generateParenthesis(self, n: int):
        s = '('
        result = []
        def f(t):
            d = {'(':0, ')':0}
            for a in t:
                d[a] += 1
            left = n-d['(']
            dif = d['('] - d[')']
            if left:
                f(t+'(')

            if dif:
                f(t + ')')

            if left == 0 and dif == 0:
                result.append(t)
        f(s)
        return result


s = Solution()
print(s.generateParenthesis(3))