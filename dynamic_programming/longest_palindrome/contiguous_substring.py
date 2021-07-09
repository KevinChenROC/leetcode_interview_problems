# +++ START YOUR IMPLEMENTATION


def len_palindrome(string):
    """
    return len(string) if string is palindrome else 0
    """
    str_len = len(string)

    # How to check
    # aaaxbaaa
    # i      j
    #  i    j
    #   i  j
    isPalindrome = True
    for i in range(str_len // 2):
        if string[i] != string[str_len - 1 - i]:
            isPalindrome = False
            break

    return str_len if isPalindrome else 0


def longest_palindrome(s):
    # Write a function to return the length of the longest palindrome
    # in an input string.
    # Ex:
    #   longest_palindrome('aab') => 2
    #   longest_palindrome('Aaab') => 2
    #   longest_palindrome('') => 0
    #   longest_palindrome('fuasdfjh123454321ddd') => 9

    s_len = len(s)
    max_len = 0

    # check for every possbile combinations
    # a a a x b a a a
    # ij
    # i j
    # i   j
    # so on...
    for i in range(s_len):
        for j in range(i, s_len):
            max_len = max(max_len, len_palindrome(s[i : j + 1]))
    return max_len


# --- START YOUR IMPLEMENTATION

print(longest_palindrome("aab"))  # 2
print(longest_palindrome("Aaab"))  # 2
print(longest_palindrome("AaaA"))  # 4
print(longest_palindrome(""))  # 0
print(longest_palindrome("aaabxaaa"))  # 3
print(longest_palindrome("fuasdfjh123454321ddd"))  # 9
