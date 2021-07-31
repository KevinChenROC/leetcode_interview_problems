
using namespace std;

class Solution
{
public:
    double myPow(double x, long n)
    {
        double ans = 1;
        bool isNeg = false;
        if (n < 0)
        {
            n = -n;
            isNeg = true;
        }

        //some edge cases
        if (n == 0)
            return 1;
        else if (x == 1)
            return x;
        else if (x == -1)
        {
            if (n % 2 == 0)
                return -x;
            else
                return x;
        }

        while (n > 1)
        {
            if (n % 2 == 1)
            {
                ans *= x;
            }

            x = x * x;
            n /= 2;
        }

        ans *= x;

        if (isNeg)
            return 1 / ans;
        else
            return ans;
    }
};
