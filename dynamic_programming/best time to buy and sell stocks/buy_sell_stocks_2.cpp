#include <vector>

using namespace std;

// Example 1 :

// Input : prices = [ 7, 1, 5, 3, 6, 4 ]
// Output : 7
// Explanation : Buy on day 2(price = 1) and sell on day 3(price = 5), profit = 5 - 1 = 4. Then buy on day 4(price = 3) and sell on day 5(price = 6), profit = 6 - 3 = 3.

class Solution
{
public:
    int maxProfit(const vector<int> &prices)
    {
        int oneTransacMaxProfit = 0, multTransacMaxProfit = 0, minNum = prices[0];
        const size_t &&lenPrices = prices.size();
        for (size_t i = 0; i < lenPrices; i++)
        {
            //find the max profit from multiple transactions
            int pricesDiff;

            if (i >= (lenPrices - 1))
                pricesDiff = 0;
            else
                pricesDiff = prices[i + 1] - prices[i];

            if (pricesDiff > 0)
            {
                multTransacMaxProfit += pricesDiff;
            }

            //maxProfit for one transcation
            if ((prices[i] - minNum) > oneTransacMaxProfit)
                oneTransacMaxProfit = prices[i] - minNum;

            minNum = min<int>(minNum, prices[i]);
        }

        return max<int>(oneTransacMaxProfit, multTransacMaxProfit);
    }
};
