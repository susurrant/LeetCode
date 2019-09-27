class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])

        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        print(matrix)
        for i in range(n):
            matrix[i].reverse()




s = Solution()
m = [[5,1,9,11],
     [2,4,8,10],
     [13,3,6,7],
     [15,14,12,16]]
s.rotate(m)
print(m)

