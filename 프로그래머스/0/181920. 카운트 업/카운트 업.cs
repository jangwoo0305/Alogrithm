using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int start_num, int end_num)
    {
        List<int> num_list = new List<int>();
        
        for (int i = start_num; i <= end_num; i++)
        {
            num_list.Add(i);
        }
        
        return num_list.ToArray();
    }
}