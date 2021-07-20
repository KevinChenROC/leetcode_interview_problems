// Given a string s, find the length of the longest substring without repeating characters.

// Example 1:

// Input: s = "abcabcbb"
// Output: 3
// Explanation: The answer is "abc", with the length of 3.
// Example 2:

// Input: s = "bbbbb"
// Output: 1
// Explanation: The answer is "b", with the length of 1.
// Example 3:

// Input: s = "pwwkew"
// Output: 3
// Explanation: The answer is "wke", with the length of 3.
// Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
// Example 4:

// Input: s = ""
// Output: 0

// Constraints:

// 0 <= s.length <= 5 * 104
// s consists of English letters, digits, symbols and spaces.

#include <string>
#include <map>
using namespace std;

class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        size_t len_s = s.length();

        if (len_s == 0 or len_s == 1)
            return len_s;

        size_t max_len = 0, i = 0, j = 0;
        map<char, int> occurence;

        while (i < len_s && j < len_s)
        {
            const char c = s[j];
            if (occurence[c] == 0)
            {
                occurence[c] = 1;
                ++j;
            }
            else
            {
                occurence[s[i]] -= 1;

                //update max_len
                max_len = ((j - i) > max_len) ? (j - i) : max_len;
                ++i;
            }
        }

        max_len = ((j - i) > max_len) ? (j - i) : max_len;
        return max_len;
    }
};

// #include <iostream>

// int main()
// {
//     map<char, int> occurence;
//     cout << occurence['a'] << endl;
// }