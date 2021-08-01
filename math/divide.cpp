#include <cmath>
#include <iostream>

using namespace std;

class Solution
{
public:
    //divide two integers without using multiplication, division, and mod operator.
    int divide(const long dividend, const long divisor)
    {

        //Edge cases
        if (dividend == INT32_MIN && divisor == -1)
        {
            return __INT_MAX__;
        }

        long dvd = labs(dividend), dvr = labs(divisor), ans = 0;
        int8_t sign = (dividend > 0) ^ (divisor > 0) ? -1 : 1;
        while (dvd >= dvr)
        {
            long temp = dvr, m = 1;
            while (dvd >= (temp << 1))
            {
                temp <<= 1;
                m <<= 1;
            }
            dvd -= temp;
            ans += m;
        }

        return sign * ans;
    }
};
