# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.


class Solution(object):
    def __maxSubArray(self, nums, start, end, table):
        # base case
        if start == end:
            return nums[start]

        if end in table[start]:
            return table[start][end]

        q = 0
        for i in range(start, end + 1):
            q += nums[i]
        table[start][end] = q

        return max(
            q,
            self.__maxSubArray(nums, start + 1, end, table),
            self.__maxSubArray(nums, start, end - 1, table),
        )

    # Recursive solution without memorization
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # edge case
        len_nums = len(nums)
        if len_nums == 1:
            return nums[0]

        # Initialize the table for memorization
        table = {}
        for i in range(len_nums):
            table[i] = {}

        return self.__maxSubArray(nums, 0, len_nums - 1, table)


sol = Solution()
print(sol.maxSubArray([1]))
print(sol.maxSubArray([5, 4, -1, 7, 8]))
print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Example 2:

# Input: nums = [1]
# Output: 1

# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
