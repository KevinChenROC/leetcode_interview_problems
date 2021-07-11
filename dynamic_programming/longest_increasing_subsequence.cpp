#include <vector>
using namespace std;

class Solution
{
public:
    int lengthOfLIS(vector<int> &nums)
    {
        size_t len_nums = nums.size();
        if (len_nums <= 1)
        {
            return len_nums;
        }

        // LIS[i] contains the maxium len of a subsequence, ending at i,
        size_t lis[len_nums];
        for (size_t i = 0; i < len_nums; i++)
            lis[i] = 1;

        for (int i = 0; i < len_nums; i++)
        {
            for (int j = i + 1; j < len_nums; j++)
            {
                if ((nums[j] > nums[i]) && (lis[j] <= lis[i]))
                    lis[j] = 1 + lis[i];
            }
        }

        // obtain the maxium len from LIS array
        int max_len = 0;
        for (size_t i = 0; i < len_nums; i++)
        {
            max_len = (lis[i] > max_len) ? lis[i] : max_len;
        }

        return max_len;
    }
};

// Example 1 :

//     Input : nums = [ 10, 9, 2, 5, 3, 7, 101, 18 ] Output : 4
// Explanation : The longest increasing subsequence is[2, 3, 7, 101],
// therefore the length is 4.

//Example 2 :

//     Input : nums = [ 0, 1, 0, 3, 2, 3 ] Output : 4

//Example 3 :

//     Input : nums = [ 7, 7, 7, 7, 7, 7, 7 ] Output : 1
