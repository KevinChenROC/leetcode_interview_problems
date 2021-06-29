class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_groups = []
        for i in range(0, len(strs)):
            # check if strs[i] is in any anagram group
            skip = False
            for l in range(0, len(anagram_groups)):
                if strs[i] in anagram_groups[l]:
                    skip = True

            # if strs[i] in any anagram group, skip to next str.
            if skip:
                continue

            anagram_group = [strs[i]]

            for j in range(i + 1, len(strs)):
                if sorted(strs[i]) == sorted(strs[j]):
                    anagram_group.append(strs[j])

            anagram_groups.append(anagram_group)

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
