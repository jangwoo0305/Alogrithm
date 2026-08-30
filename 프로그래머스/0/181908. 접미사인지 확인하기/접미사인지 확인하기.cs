using System;
using System.Collections.Generic;

public class Solution {
    public int solution(string my_string, string is_suffix)
    {
        List<string> answer = new List<string>();
        
        for (int i = 0; i < my_string.Length; i++)
        {
            answer.Add(my_string.Substring(i));
        }
        
        for (int i = 0; i < answer.Count; i++)
        {
            if (answer[i] == is_suffix)
            {
                return 1;
            }
        }
        
        return 0;
    }
}