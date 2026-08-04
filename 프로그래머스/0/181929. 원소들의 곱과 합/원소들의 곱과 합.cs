using System;

public class Solution 
{
    public int solution(int[] num_list) 
    {
        int a = 0;
        int b = 1;

        for(int idx = 0; idx < num_list.Length; idx++)
        {
            a += num_list[idx];
            b *= num_list[idx];
        }

        return b < a*a ? 1 : 0;
    }
}