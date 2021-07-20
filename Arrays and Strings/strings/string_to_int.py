# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

# The algorithm for myAtoi(string s) is as follows:

# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
# Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
# If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -2^31 should be clamped to -2^31, and integers greater than 2^31 - 1 should be clamped to 2^31 - 1.
# Return the integer as the final result.
# Note:

# Only the space character ' ' is considered a whitespace character.
# Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.


def isDigit(c):
    return True if (c >= "0" and c <= "9") else False


class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # print("=================")

        index = 0
        len_s = len(s)
        # 1. skip leading whitespaces
        while index < len_s:
            if s[index] == " ":
                index += 1
            else:
                break

        # 2. before the first digit, read - or + if any
        if index < len_s:
            positive = True
            sign = s[index]
        else:
            return 0

        if sign == "+" or sign == "-":
            index += 1
            if sign == "-":
                positive = False

        # 3. read in the digits
        digits = ""
        len_digits = 0
        while index < len_s and isDigit(s[index]):
            digits += s[index]
            len_digits += 1
            index += 1

        # print("Digits: +" + digits) if positive else print("Digits: -" + digits)
        # print("len_digits: " + str(len_digits))
        # 4. convert digits to int, and check the int is within the limits.
        if len_digits == 0:
            return 0

        integer = 0
        upper_limit = 2 ** 31 - 1
        lower_limit = -(2 ** 31)

        for i in reversed(range(len_digits)):
            power = len_digits - i - 1
            int_to_add = int(digits[i]) * (10 ** power)

            # print("before addition, current integer : " + str(integer))
            # print("int_to_add: " + str(int_to_add))
            if positive:
                if abs(upper_limit - integer) < int_to_add:
                    return upper_limit
                integer += int_to_add
            else:
                if abs(lower_limit - integer) < int_to_add:
                    return lower_limit
                integer -= int_to_add
            pass
        return integer


sol = Solution()

s = ""
print(sol.myAtoi(s))

s = "42"
print(sol.myAtoi(s))
# Output: 42
# Explanation: The underlined characters are what is read in, the caret is the current reader position.
# Step 1: "42" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "42" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "42" ("42" is read in)
#            ^
# The parsed integer is 42.
# Since 42 is in the range [-2^31, 2^31 - 1], the final result is 42.

# Example 2:

s = "   -42"
print(sol.myAtoi(s))
# Output: -42
# Explanation:
# Step 1: "   -42" (leading whitespace is read and ignored)
#             ^
# Step 2: "   -42" ('-' is read, so the result should be negative)
#              ^
# Step 3: "   -42" ("42" is read in)
#                ^
# The parsed integer is -42.
# Since -42 is in the range [-2^31, 2^31 - 1], the final result is -42.

# Example 3:

s = "4193 with words"
print(sol.myAtoi(s))
# Output: 4193
# Explanation:
# Step 1: "4193 with words" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
#              ^
# The parsed integer is 4193.
# Since 4193 is in the range [-2^31, 2^31 - 1], the final result is 4193.
# Example 4:

s = "words and 987"
print(sol.myAtoi(s))
# Output: 0
# Explanation:
# Step 1: "words and 987" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "words and 987" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "words and 987" (reading stops immediately because there is a non-digit 'w')
#          ^
# The parsed integer is 0 because no digits were read.
# Since 0 is in the range [-2^31, 2^31 - 1], the final result is 0.

# Example 5:

s = "-91283472332"
print(sol.myAtoi(s))
# Output: -2147483648
# Explanation:
# Step 1: "-91283472332" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "-91283472332" ('-' is read, so the result should be negative)
#           ^
# Step 3: "-91283472332" ("91283472332" is read in)
#                      ^
# The parsed integer is -91283472332.
# Since -91283472332 is less than the lower bound of the range [-231, 231 - 1], the final result is clamped to -231 = -2147483648.
