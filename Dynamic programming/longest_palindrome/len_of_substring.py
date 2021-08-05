# a substring of a string S is a CONTIGUOUS subsequence of S


def longest_palindrome(s):
    # Write a function to return the length of the longest palindrome
    # in an input string.
    # Ex:
    #   longest_palindrome('aab') => 2
    #   longest_palindrome('Aaab') => 2
    #   longest_palindrome('') => 0
    #   longest_palindrome('fuasdfjh123454321ddd') => 9

    len_s = len(s)

    # check for edge case
    if len_s == 0 or len_s == 1:
        return len_s

    # If isPalindrome[i][j] is True --> s[i:j+1] is palindrome
    # e.g. "abb" => isPalindrome[1][2] is True
    isPalindrome = [[False] * len_s for _ in range(len_s)]

    # s[i:i+1] is always a palindrome
    for i in range(len_s):
        isPalindrome[i][i] = True

    # Example of how it works
    # Let s = "Abab"
    # 0  1  2  3
    # A  b  a  b
    #       i  j isPalindrome[2][3] = False
    #    i  j    isPalindrome[1][2] = False
    #    i     j isPalindrome[1][3] = isPalindrome[2][2] = True
    #                                         --> max_len = j-i+1
    # i  j       isPalindrome[0][1] = False
    # i     j    isPalindrome[0][2] = False
    # i        j isPalindrome[0][3] = False

    max_len = 1
    for i in range(len_s - 2, -1, -1):
        for j in range(i + 1, len_s):
            if s[i] == s[j]:
                if j - i > 2:
                    isPalindrome[i][j] = isPalindrome[i + 1][j - 1]
                else:
                    isPalindrome[i][j] = True

                if isPalindrome[i][j]:

                    max_len = max((j - i + 1), max_len)

    return max_len


# --- START YOUR IMPLEMENTATION

print(longest_palindrome(""))  # 0
print(longest_palindrome("bx"))  # 1
print(longest_palindrome("aab"))  # 2
print(longest_palindrome("Aaab"))  # 2
print(longest_palindrome("AaaA"))  # 4
print(longest_palindrome("aabxaa"))  # 2
print(longest_palindrome("fuasdfjh123454321ddd"))  # 9
