# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.


class Solution(object):

    # Recursive solution without memorization
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        q = 0
        for num in nums:
            q += num

        return max(q, self.maxSubArray(nums[:-1]), self.maxSubArray(nums[1:]))


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
