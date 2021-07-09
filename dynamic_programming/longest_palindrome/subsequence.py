class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        lps = [[0] * n for _ in range(n)]  # create lps[n][n]

        for i in range(n):
            lps[i][i] = 1

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    lps[i][j] = lps[i + 1][j - 1] + 2
                else:
                    lps[i][j] = max(lps[i][j - 1], lps[i + 1][j])

        return lps[0][n - 1]


sol = Solution()
print(sol.longestPalindromeSubseq("bbbab"))
print(sol.longestPalindromeSubseq("bbbaxbbb"))
