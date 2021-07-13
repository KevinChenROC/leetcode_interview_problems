# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        occurence = {}
        index = {}

        # Populate index and occurrence maps
        for i in range(0, len(nums)):
            num = nums[i]
            if num not in index:
                index[num] = [i]
            else:
                index[num].append(i)

            if num not in occurence:
                occurence[num] = 1
            else:
                occurence[num] += 1
        # print("occurence " + str(occurence))
        # print("index " + str(index))

        for i in range(0, len(nums)):
            x = nums[i]
            y = target - x

            if x == y:
                if occurence[x] >= 2:
                    return index[y][0:2]
                else:
                    continue
            elif y in occurence:
                return [i, index[y][0]]

        return None


sol = Solution()

# Example 1:
nums = [2, 7, 11, 15]
target = 9
print(sol.twoSum(nums, target))
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2
nums = [3, 2, 4]
target = 6
print(sol.twoSum(nums, target))
# Output: [1,2]


# Example 3:
nums = [3, 3]
target = 6
sol = Solution()
print(sol.twoSum(nums, target))
# Output: [0,1]

nums = [3, 2, 4, 8, 8]
target = 6
print(sol.twoSum(nums, target))
# Output: [1,2]
