#include <iostream>
#include <string>
using namespace std;

// Example 1 :

//     Input : s = "babad" Output : "bab" Note : "aba" is also a valid answer.

// Example 2 :

//     Input : s = "cbbd" Output : "bb"

// Example 3 :

//     Input : s = "a" Output : "a"

// Example 4 :

//     Input : s = "ac" Output : "a"

class Solution
{
public:
    string longestPalindrome(string s)
    {
        size_t len_s = s.length();
        //check edge cases
        if (len_s == 0 || len_s == 1)
        {
            return s;
        }

        // initialize the dynamic table
        bool is_palindrome[len_s][len_s];

        for (size_t i = 0; i < len_s; i++)
        {
            for (size_t j = 0; j < len_s; j++)
            {
                if (i == j)
                    is_palindrome[i][j] = true;
                else
                    is_palindrome[i][j] = false;
            }
        }

        size_t max_len = 1;
        size_t left = 0;  //leftmost idx of the palindrom
        size_t right = 0; //rightmost idx of the palindrom

        for (int i = len_s - 1; i >= 0; --i)
        {
            for (int j = i + 1; j < len_s; ++j)
            {
                if (s[i] == s[j])
                {
                    if (j - i > 1)
                        is_palindrome[i][j] = is_palindrome[i + 1][j - 1];
                    else
                        is_palindrome[i][j] = true;

                    if (is_palindrome[i][j])
                    {
                        if ((j - i + 1) > max_len)
                        {
                            max_len = j - i + 1;
                            left = i, right = j;
                        }
                    }
                }
                // cout << i << endl;
                // cout << j << endl;
            }
        }

        return s.substr(left, max_len);
    }
};

// int main()
// {
//     Solution sol;
//     cout << sol.longestPalindrome("badad") << endl;
//     // cout << occurence['a'] << endl;
//     return 0;
// }

// Line 1061 : Char 9 : runtime error : addition of unsigned offset to 0x7ffc932c4ee0 overflowed to 0x7ffc932c4edf(basic_string.h)
//                                          SUMMARY : UndefinedBehaviorSanitizer : undefined
//                                                                                 -
//                                                                                 behavior / usr / bin /../ lib / gcc / x86_64 - linux - gnu / 9 /../../../../ include / c++ / 9 / bits / basic_string.h : 1070 : 9