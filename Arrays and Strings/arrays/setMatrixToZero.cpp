#include <vector>

using namespace std;

class Solution
{
public:
    //Big idea
    //  The first cell of ith row or jth col is a flag
    //  If the flag is 0, then set the ith row or jth col to zero
    void setZeroes(vector<vector<int>> &matrix)
    {

        // m = number of rows
        // n = number of columns
        size_t m = matrix.size(), n = matrix[0].size();

        //set up flags
        bool firstColZeros = false;
        for (size_t i = 0; i < m; i++)
        {
            if (matrix[i][0] == 0)
                firstColZeros = true;
            for (size_t j = 1; j < n; j++)
            {
                if (matrix[i][j] == 0)
                {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }

        for (size_t i = 1; i < m; i++)
        {
            for (size_t j = 1; j < n; j++)
            {
                if (matrix[i][0] == 0 || matrix[0][j] == 0)
                    matrix[i][j] = 0;
            }
        }
        //update first row
        if (matrix[0][0] == 0)
        {
            for (size_t j = 1; j < n; j++)
                matrix[0][j] = 0;
        }

        //update first colum
        if (firstColZeros)
        {
            for (size_t i = 0; i < m; i++)
                matrix[i][0] = 0;
        }
    }
};
