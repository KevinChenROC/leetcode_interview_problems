#include <stdio.h>

int main()
{
    int N = 100;
    for (int i = 1; i <= N; i++)
    {
        char isPrime = 1;
        for (int j = 2; j < i; j++)
        {
            if (i%j == 0)
            {
                isPrime = 0; //not a prime
                break;
            }
            
        }

        if(isPrime)
            printf("%d\n", i);

        
    }
    
    return 0;
}
