using System;

public class Solution
{
    public int solution(int[] num_list)
    {
        int answer = 0;
        string a = "";
        string b = "";
        
        for (int idx = 0; idx < num_list.Length; idx++)
        {
            if(num_list[idx] % 2 == 0)
                a += num_list[idx].ToString();
            else
                b += num_list[idx].ToString();
        }
        
        int c = int.Parse(a);
        int d = int.Parse(b);
        
        return c + d;
    }
}