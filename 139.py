class Solution:
    def wordBreak(self, s, wordDict) -> bool:
        d = set(wordDict)
        m = [None]*len(s)

        def f(ins, idx):
            if idx == len(ins):
                return True

            if m[idx]:
                return m[idx]

            j = idx
            while j < len(ins)+1:
                if ins[idx:j] in d and f(ins, j):
                    m[idx] = True
                    return m[idx]
                j += 1

            m[idx] = False
            return m[idx]

        return f(s, 0)

s = Solution()
print(s.wordBreak(s = "leetcode", wordDict = ["leet", "code"]))