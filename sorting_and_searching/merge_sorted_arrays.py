# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


# Constraints:

# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -109 <= nums1[i], nums2[j] <= 109


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None. Do not return anything, modify nums1 in-place instead.
        """
        i = j = k = 0
        sorted_arr = [0] * (m + n)
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                sorted_arr[k] = nums1[i]
                i += 1
            else:
                sorted_arr[k] = nums2[j]
                j += 1
            k += 1

        if i < m:
            for num in nums1[i:m]:
                sorted_arr[k] = num
                k += 1

        elif j < n:
            for num in nums2[j:n]:
                sorted_arr[k] = num
                k += 1

        # copy sorted_arr to nums1 in place
        for idx, num in enumerate(sorted_arr):
            nums1[idx] = num


# sol = Solution()
# nums1 = [0]
# sol.merge(nums1, 0, [1], 1)
# print(nums1)
