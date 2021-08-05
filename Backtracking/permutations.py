# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Constraints
#     1 <= nums.length <= 6
#     -10 <= nums[i] <= 10
#     All the integers of nums are unique.


def copy_by_append(from_list, to_list):
    for item in from_list:
        to_list.append(item)
    return to_list


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permutations = []
        IDX = 1
        LIST = 0

        for num in nums:
            idx = nums.index(num)
            init_adj_list = nums[:idx] + nums[idx + 1 :]  # This should be immutable
            adj_list = {
                num: [init_adj_list, 0]
            }  # each num is associated with (adj_list, cur_idx on the adj_list)
            curr_num = num
            path = [num]

            while path:
                if not adj_list[curr_num][LIST]:
                    permutations.append(
                        copy_by_append(path, [])
                    )  # please copy by value
                    path.pop()
                    if path:
                        adj_list[path[-1]][IDX] += 1
                        curr_num = path[-1]
                    continue

                adj_idx = adj_list[curr_num][IDX]

                # check if adj_idx is out of range
                if adj_idx < len(adj_list[curr_num][LIST]):
                    next_num = adj_list[curr_num][LIST][adj_idx]
                    next_adj_list = (
                        adj_list[curr_num][LIST][:adj_idx]
                        + adj_list[curr_num][LIST][adj_idx + 1 :]
                    )

                    adj_list[next_num] = [next_adj_list, 0]
                    path.append(next_num)
                    curr_num = next_num
                else:
                    # if adj_idx is out of range, simply backtrack
                    path.pop()
                    if path:
                        adj_list[path[-1]][IDX] += 1
                        curr_num = path[-1]

        return permutations


# sol = Solution()
# print(sol.permute([1, 2, 3]))
# print(sol.permute([1, 2]))
# print(sol.permute([1]))
