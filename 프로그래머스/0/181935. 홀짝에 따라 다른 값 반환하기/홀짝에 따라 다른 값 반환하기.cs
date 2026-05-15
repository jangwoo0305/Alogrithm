using System;

public class Solution
{
    public int solution(int n)
    {   
        if (n % 2 == 1)
        {
            int sum = 0;
            for (int i = 0; i <= n; i++)
            {
                if (i % 2 == 1)
                    sum += i;
            }
        return sum;
        }
        else
        {
            int sum = 0;
            for (int i = 0; i <= n; i++)
            {
                if (i % 2 == 0)
                    sum += i * i;
            }
        return sum;
        }   
    }
}