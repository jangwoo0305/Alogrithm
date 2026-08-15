using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int n) 
    {
        List<int> num_list = new List<int>();
        
        num_list.Add(n);
        
        while(n != 1)
        {
            if(n % 2 == 0)
            {
                n = n / 2;
                num_list.Add(n);
            }
            else
            {
                n = ( 3 * n ) + 1;
                num_list.Add(n);
            }
        }
        
        return num_list.ToArray();
    }
}