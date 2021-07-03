# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        global_max, curr_sum = -(2 ** 31), 0
        for i in range(len(nums)):
            # if curr_sum becomes negative, it has no use for the next element, so we restart curr_sum from 0 again.
            if curr_sum + nums[i] < 0:
                curr_sum, global_max = 0, max(global_max, nums[i])
            else:
                # if curr_sum > 0, it's possible to make it bigger so we keep curr_sum.
                curr_sum, global_max = curr_sum + nums[i], max(
                    global_max, curr_sum + nums[i]
                )
        return global_max


sol = Solution()
print(sol.maxSubArray([1]))
print(sol.maxSubArray([5, 4, -1, 7, 8]))
print(sol.maxSubArray([-5, -4, -1, -7, -8]))
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
