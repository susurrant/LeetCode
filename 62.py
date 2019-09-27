class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n)] for j in range(m)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i+1 < m and j+1 < n:
                    dp[i][j] = dp[i+1][j]+dp[i][j+1]
                elif i+1 == m and j+1 < n:
                    dp[i][j] = dp[i][j+1]
                elif i+1 < m and j+1 == n:
                    dp[i][j] = dp[i+1][j]
                else:
                    dp[i][j] = 1

        return dp[0][0]

s = Solution()
print(s.uniquePaths(7,3))