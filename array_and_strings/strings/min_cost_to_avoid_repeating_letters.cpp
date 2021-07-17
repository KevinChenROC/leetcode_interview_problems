// Given

// a string s and an array of integers cost where cost[i] is the cost of deleting the ith character in s.

// FIND:

//the minimum cost of deletions such that there are no two identical letters next to each other.

// Notice that you will delete the chosen characters at the same time, in other words, after deleting a character, the costs of deleting other characters will not change.

// Example 1:

// Input: s = "abaac", cost = [1,2,3,4,5]
// Output: 3
// Explanation: Delete the letter "a" with cost 3 to get "abac" (String without two identical letters next to each other).

// Example 2:

// Input: s = "abc", cost = [1,2,3]
// Output: 0
// Explanation: You don't need to delete any character because there are no identical letters next to each other.

// Example 3:

// Input: s = "aabaa", cost = [1,2,3,4,1]
// Output: 2
// Explanation: Delete the first and the last character, getting the string ("aba").

// Constraints:

/*   s.length == cost.length
     1 <= s.length, cost.length <= 10^5
     1 <= cost[i] <= 10^4
     s contains only lowercase English letters.
*/

#include <iostream>
#include <vector>
using namespace std;

class Solution
{
private:
    int findMax(vector<int> &cost, int i, int k)
    {
        int max_cost = 0;
        while (i <= k)
        {
            max_cost = cost[i] > max_cost ? cost[i] : max_cost;
            i++;
        }

        return max_cost;
    }

public:
    int minCost(string s, vector<int> &cost)
    {
        //

        size_t len_s = s.size();

        //check edge cases
        if (len_s <= 1)
            return 0;

        int i = 0, j = 0;
        int total_cost = 0;
        int potential_cost = 0;

        // sum over a substring of the same letters,
        // then substract the one with the highest cost from the sum
        // this gives you the cost of removing the same letters over this substring.
        // repeat the process.

        while (j < len_s)
        {
            if (s[i] == s[j])
            {
                potential_cost += cost[j];
                j++;
            }
            else
            {
                potential_cost -= findMax(cost, i, j - 1);
                total_cost += potential_cost;
                potential_cost = 0;
                i = j;
            }
        }

        // treat the special case at the tail of s
        if (j - i > 1)
        {

            total_cost += potential_cost - findMax(cost, i, j - 1);
        }
        return total_cost;
    }
};

// "dbacd"
// [10, 5, 2, 2, 2]
// "aaac"
// [3, 1, 4, 1]
// "abaac"
// [1, 2, 3, 4, 5]