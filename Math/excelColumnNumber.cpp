#include <string>
using namespace std;

class Solution
{
public:
    int titleToNumber(string columnTitle)
    {
        //loop over columnTitle, turn each char into a number
        //A->1, B->2, ... Z->26, AA->27, AB->28, ...
        long ans = 0;
        for (auto &&c : columnTitle)
        {
            ans = ans * 26 + (int)c - 64;
        }

        return ans;
    }
};

// Example 1 :

//     Input : columnTitle = "A" Output : 1

// Example 2 :

//     Input : columnTitle = "AB" Output : 28

// Example 3 :

//     Input : columnTitle = "ZY" Output : 701

// Example 4 :

//     Input : columnTitle = "FXSHRXW" Output : 2147483647

// "AAA" --> 703

//26+26*26+1

#include <iostream>

int main(int argc, char const *argv[])
{
    string s = "123";
    char *cPtr = &(s[0]);
    cout << *cPtr;
    return 0;
}
