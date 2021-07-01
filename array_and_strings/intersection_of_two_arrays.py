class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        # Create a map occurrence from nums1
        occurence = {}
        for num in nums1:
            if num not in occurence:
                occurence[num] = 1
            else:
                occurence[num] += 1

        intersects = []
        # Iterate over nums2 to find intersections
        for num in nums2:
            if num in occurence:
                intersects.append(num)
                occurence[num] -= 1
                if occurence[num] == 0:
                    del occurence[num]

        return intersects
