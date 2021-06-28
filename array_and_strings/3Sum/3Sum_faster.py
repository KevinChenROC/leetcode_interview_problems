class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Obtain a map num_map from nums
        # Double loops over the keys
        # Check if num_map[i] >= 2

        num_map = {}
        for i in nums:
            if i not in num_map:
                num_map[i] = 1
            elif num_map[i] >= 3:
                continue
            else:
                num_map[i] += 1
        print(num_map)

        triplets = []

        num_keys = list(num_map.keys())
        num_keys.sort()
        # print("num_keys " + str(num_keys))
        LEN = len(num_keys)

        for i in range(0, LEN):
            # check for special cases
            num_key_i = num_keys[i]
            if num_map[num_key_i] >= 2:
                value = 0 - 2 * num_key_i

                # to avoid duplication
                if value < num_key_i:
                    continue

                # print(str(num_key_i) + ": " + str(num_map[num_key_i]))
                ## [0,0,0] cases
                if num_key_i == 0:
                    if num_map[value] >= 3:
                        triplets.append([num_key_i] * 3)
                ## All other cases
                elif value in num_map and num_key_i != 0:
                    # print("add once")
                    triplets.append([num_key_i] * 2 + [value])

            for j in range(i + 1, LEN):
                num_key_j = num_keys[j]
                value = 0 - num_key_i - num_key_j

                # to avoid duplication
                if value in num_map and value > num_key_i and value >= num_key_j:
                    # print(num_key_i)
                    # print([num_key_i, num_key_j, value])

                    # check for cases [num_key_i, value, value]
                    if value == num_key_j and num_map[value] < 2:
                        continue

                    triplets.append([num_key_i, num_key_j, value])
                pass

        return triplets


nums1 = [-1, 0, 1, 2, -1, -4]
nums2 = [-1, 0, 1, 2]
nums3 = [
    0,
    -1,
    -1,
    0,
    1,
    2,
    -1,
    -1,
    -1,
]
nums4 = [-2, -2, 0, 1, 1, 1, 2, 2, -4]
nums5 = [-1, 0, 1, 2, -1, -4]  # expected [[-1,-1,2],[-1,0,1]]
nums6 = [0, 0, 0]

sol = Solution()
print(sol.threeSum(sorted(nums6)))
