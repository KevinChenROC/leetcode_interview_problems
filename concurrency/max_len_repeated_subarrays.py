class Solution(object):
    # basic recursion solution
    # def findLength_recursion(self, nums1, nums2):
    #     """
    #     :type nums1: List[int]
    #     :type nums2: List[int]
    #     :rtype: int
    #     """
    #     if not nums1 or not nums2:
    #         return 0

    #     max_len = max(
    #         self.findLength(nums1[1:], nums2), self.findLength(nums1, nums2[1:])
    #     )

    #     if nums1[0] == nums2[0]:
    #         return max(max_len, 1 + self.findLength(nums1[1:], nums2[1:]))
    #     else:
    #         return max_len

    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m = len(nums1)
        n = len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_len = 0
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                    max_len = max(max_len, dp[i][j])
        return max_len


# sol = Solution()
# print(sol.findLength([1, 2, 3], [4, 1, 2, 3]))
# print(sol.findLength([0, 1, 1, 1, 1], [1, 0, 1, 0, 1]))
# print(sol.findLength([1, 0, 0, 0, 1], [1, 0, 0, 1, 1]))  # expect 3
