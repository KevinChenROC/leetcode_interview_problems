#include <iostream>
#include <string>
#include <map>

using namespace std;

// Given a string, find the first non-repeating character(lowercase only a~z) in it and return it's index. If it doesn't exist, return -1.

// Examples:

// s = "loveetd" return 0.
// s = "etdisetd", return 3.

int firstUniqChar(string str) // C++
{
    map<char, int> occurence;

    const int str_len = str.length();
    for (size_t i = 0; i < str_len; i++)
    {
        occurence[str[i]] += 1;
    }

    int first_unique_char_idx = -1;
    for (size_t i = 0; i < str_len; i++)
    {
        if (occurence[str[i]] == 1)
        {
            first_unique_char_idx = i;
            break;
        }
    }
    return first_unique_char_idx;
}

int main()
{

    // map<int, int> occurence;
    // for (size_t i = 0; i < 10; i++)
    // {
    //     /* code */
    //     if (occurence[i] != 0)
    //     {
    //         cout << occurence[i];
    //     }
    // }
    // for (size_t i = 0; i < 10; i++)
    // {
    //     cout << occurence[i];
    // }

    cout << firstUniqChar("loveetd") << endl;
    cout << firstUniqChar("etdisetd") << endl;
    cout << firstUniqChar("loveleetcode") << endl;

    return 0;
}