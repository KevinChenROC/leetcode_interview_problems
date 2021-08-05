class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        triplets = []
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if (nums[i] + nums[j] + nums[k]) == 0:
                        triplet_to_add = [nums[i], nums[j], nums[k]]
                        triplet_to_add.sort()
                        if len(triplets) == 0:
                            # print("should appear once")
                            triplets.append(triplet_to_add)
                            continue

                        # Append the current triplet if no duplication
                        duplication = False
                        for l in range(0, len(triplets)):
                            triplet = triplets[l]
                            triplet.sort()
                            if triplet_to_add == triplet:
                                duplication = True
                                break
                        if not duplication:
                            triplets.append(triplet_to_add)
                    pass

        return triplets


nums1 = [-1, 0, 1, 2, -1, -4]
nums2 = [-1, 0, 1, 2]
nums3 = [-1, -1, -1, -1, -1, 0, 1, 2]

sol = Solution()
print(sol.threeSum(nums2))
