// Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

// Example 1:

// Input: nums = [1,2,3,4,5]
// Output: true
// Explanation: Any triplet where i < j < k is valid.
// Example 2:

// Input: nums = [5,4,3,2,1]
// Output: false
// Explanation: No triplet exists.
// Example 3:

// Input: nums = [2,1,5,0,4,6]
// Output: true
// Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

// Constraints:

// 1 <= nums.length <= 5 * 105
// -231 <= nums[i] <= 231 - 1

// Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?

#include <iostream>
#include <vector>
#include <climits>

using namespace std;

class Solution
{
public:
    // check if there is a sequence (i,j,k ) such that
    // 1. i<j<k
    // 2. nums[i] < nums[j] < nums[k]
    bool increasingTriplet(vector<int> &nums)
    {
        int c1 = INT_MAX, c2 = INT_MAX;
        for (int x : nums)
        {
            if (x <= c1)
            {
                c1 = x; // c1 is min seen so far (it's a candidate for 1st element)
            }
            else if (x <= c2)
            {           // here when x > c1, i.e. x might be either c2 or c3
                c2 = x; // x is better than the current c2, store it
            }
            else
            {                // here when we have/had c1 < c2 already and x > c2
                return true; // the increasing subsequence of 3 elements exists
            }
        }
        return false;
    }
};