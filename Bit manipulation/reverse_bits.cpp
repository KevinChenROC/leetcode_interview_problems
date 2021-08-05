#include <iostream>
#include <cmath>

// Example 1 :

//     Input : n = 00000010100101000001111010011100 Output : 964176192(00111001011110000010100101000000)
//                 Explanation : The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596,
//             so return 964176192 which its binary representation is 00111001011110000010100101000000.

// Example 2 :

//     Input : n = 11111111111111111111111111111101 Output : 3221225471(10111111111111111111111111111111)
//                 Explanation : The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293,
//             so return 3221225471 which its binary representation is 10111111111111111111111111111111.

class Solution
{
public:
    uint32_t reverseBits(uint32_t n)
    {
        const size_t N = 32; // N = 32 bits
        bool bits[N];

        // construct an array of bits
        for (size_t i = 0; i < N; i++)
        {
            if (n % 2 == 1)
            {
                bits[i] = true;
            }
            else
            {
                bits[i] = false;
            }

            n /= 2;
        }

        //reverse the array bits
        for (size_t i = 0; i < N / 2; i++)
        {
            /* code */
            bool tmp = bits[i];
            bits[i] = bits[N - 1 - i];
            bits[N - 1 - i] = tmp;
        }

        //create the output "sum" from bits
        uint32_t sum = 0;
        for (size_t i = 0; i < N; i++)
        {
            if (bits[i])
            {
                sum += pow(2, i);
            }
        }

        return sum;
    }
};