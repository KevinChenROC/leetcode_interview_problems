# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Clarification:

# What should we return when needle is an empty string? This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
# Constraints:

# 0 <= haystack.length, needle.length <= 5 * 104
# haystack and needle consist of only lower-case English characters.


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len_needle = len(needle)
        len_haystack = len(haystack)

        if len_needle == 0:
            return 0

        for i in range(0, len_haystack - len_needle + 1):
            if needle == haystack[i : i + len_needle]:
                return i

        return -1


sol = Solution()

# Example 1:
haystack = "hello"
needle = "ll"
print(sol.strStr(haystack, needle))
# Output: 2

# Example 2:

haystack = "aaaaa"
needle = "bba"
print(sol.strStr(haystack, needle))
# Output: -1

# Example 3:

haystack = ""
needle = ""
print(sol.strStr(haystack, needle))
# Output: 0
