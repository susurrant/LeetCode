class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        r = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                del stack[-1]
                if stack:
                    l = i-stack[-1]
                    r = max(l, r)
                else:
                    stack.append(i)
        return r


s = Solution()
a = ")()())()()("
print(s.longestValidParentheses(a))
