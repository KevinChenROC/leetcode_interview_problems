#include <vector>
#include <iostream>

using namespace std;

// Given:
// a large sample of integers in the range[0, 255].Since the sample is so large, it is represented by an array count where count[k] is the number of times that k appears in the sample.

// Return
// [minimum, maximum, mean, median, mode].Answers within 10^-5 of the actual answer will be accepted.

#define MIN 0
#define MAX 1
#define MEAN 2
#define MEDIAN 3
#define MODE 4
class Solution
{
public:
    static double findMedian(vector<int> &count, size_t totalCount)
    {
        size_t medianCount, curCount = 0;

        bool takeAvg;
        if (totalCount % 2 == 1)
        {
            takeAvg = false;
            medianCount = totalCount / 2 + 1;
        }
        else
        {
            takeAvg = true;
            medianCount = totalCount / 2;
        }

        size_t i = 0, sum = 0;
        for (; i < count.size(); i++)
        {
            if (count[i] > 0)
                curCount += count[i];

            if (curCount >= medianCount)
            {
                if (!takeAvg)
                    return i;
                else if (takeAvg && ((curCount - medianCount) >= 1))
                    return i;
                else
                {
                    sum += i;
                    break;
                }
            }
        }

        //try to find the next item to compute the medium
        for (i = i + 1; i < count.size(); i++)
        {
            if (count[i] > 0)
            {
                sum += i;
                break;
            }
        }
        return ((double)sum) / 2;
    }

    vector<double> sampleStats(vector<int> &count)
    {
        size_t sum = 0, mode = 0, maxCount = 0, totalCount = 0;
        vector<double> stat(5, 0.0);

        size_t i = 0;

        //first find the min, and stops.
        for (i = 0; i < count.size(); i++)
        {
            if (count[i] > 0)
            {
                stat[MIN] = i;
                break;
            }
        }

        //from i to count.size-1
        //find median, max, mode
        for (; i < count.size(); i++)
        {
            size_t curCount = count[i];
            if (curCount > 0)
            {
                sum += curCount * i;
                totalCount += curCount;
                stat[MAX] = i;
                if (curCount > maxCount)
                {
                    mode = i;
                    maxCount = curCount;
                }
            }
        }

        stat[MEAN] = (double)sum / (double)totalCount;
        stat[MODE] = mode;
        stat[MEDIAN] = findMedian(count, totalCount);

        return stat;
    }
};
