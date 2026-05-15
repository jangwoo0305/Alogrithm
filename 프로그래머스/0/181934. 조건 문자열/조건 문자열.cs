using System;

public class Solution
{
    public int solution(string ineq, string eq, int n, int m)
    {
        if(ineq == ">")
        {
            if (eq == "=")
            {
                return n >= m ? 1 : 0;
            }
            else
            {
                return n > m ? 1 : 0;
            }
        }
        else //(ineq == "<")
        {
            if(eq == "=")
            {
                return n <= m ? 1 : 0; // n <= m
            }
            else
            {
                return n < m ? 1 : 0;//n < m
            }
        }
    }
}