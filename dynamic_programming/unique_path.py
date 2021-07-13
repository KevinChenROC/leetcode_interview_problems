class Solution(object):
    # def uniquePaths_recursive(self, m, n):
    #     """
    #     :type m: int
    #     :type n: int
    #     :rtype: int
    #     """
    #     # reach the finish line
    #     if m == 1 and n == 1:
    #         return 1
    #     elif m == 0:
    #         return 0
    #     elif n == 0:
    #         return 0

    #     return self.uniquePaths_recursive(m - 1, n) + self.uniquePaths_recursive(
    #         m, n - 1
    #     )

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # create a table dp[i][j] denotes the num of unique paths with i rows and j cols

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[1][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i - 1 > 0:
                    dp[i][j] += dp[i - 1][j]
                if j - 1 > 0:
                    dp[i][j] += dp[i][j - 1]

        return dp[m][n]
