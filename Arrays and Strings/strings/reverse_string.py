# Write a function that reverses a string. The input string is given as an array of characters.

## Reversing a string is a classic example of two-pointer technique for iteration


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        len_string = len(s)
        for i in range(0, len_string // 2):
            temp = s[i]
            s[i] = s[len_string - i - 1]
            s[len_string - i - 1] = temp


sol = Solution()

# Example 1:
s = ["h", "e", "l", "l", "o"]
sol.reverseString(s)
print(s)
# Output: ["o","l","l","e","h"]

# Example 2:
s = ["H", "a", "n", "n", "a", "h"]
sol.reverseString(s)
print(s)
# Output: ["h","a","n","n","a","H"]
