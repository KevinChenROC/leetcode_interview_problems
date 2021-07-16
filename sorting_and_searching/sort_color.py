# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.


# (red, whie, blue) = (0,1,2)

# You must solve this problem without using the library's sort function.


# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]

# Example 3:

# Input: nums = [0]
# Output: [0]

# Example 4:

# Input: nums = [1]
# Output: [1]


# Constraints:

# n == nums.length
# 1 <= n <= 300
# nums[i] is 0, 1, or 2.


# Follow up: Could you come up with a one-pass algorithm using only constant extra space?


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # (R,W,B) = (0,1,2)
        R, W, B = 0, 1, 2

        len_nums = len(nums)
        if len_nums <= 1:
            return

        # use map "count" to count # of R,W,B
        count = {}
        for i in range(len_nums):
            color = nums[i]
            if color not in count:
                count[color] = 1
            else:
                count[color] += 1

        # for i=0 to len_nums-1 to replace nums with the map
        idx = 0
        for color in (R, W, B):
            if color not in count:
                continue
            
            for _ in range(count[color]):
                nums[idx] = color
                idx += 1
