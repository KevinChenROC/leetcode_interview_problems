class Solution(object):
    def sort_string(self, s):
        s = sorted(s)
        sorted_str = ""
        for letter in s:
            sorted_str += letter

        return sorted_str

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_groups = []
        group_indices = {}
        group_index = 0
        for i in range(0, len(strs)):
            sorted_str = self.sort_string(strs[i])

            if sorted_str not in group_indices:
                group_indices[sorted_str] = group_index
                anagram_groups.append([strs[i]])
                group_index += 1
            else:
                index_to_append = group_indices[sorted_str]
                anagram_groups[index_to_append].append(strs[i])
            pass

        return anagram_groups


sol = Solution()

strs = ["eat", "tea"]
print(sol.groupAnagrams(strs))
# Output: [["eat","tea"]]

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(sol.groupAnagrams(strs))
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

strs = [""]
print(sol.groupAnagrams(strs))
# Output: [[""]]

strs = ["a"]
print(sol.groupAnagrams(strs))
# Output: [["a"]]

strs = ["", ""]
print(sol.groupAnagrams(strs))
# [["",""]]


strs = ["c", "c"]
print(sol.groupAnagrams(strs))
# [["c","c"]]
