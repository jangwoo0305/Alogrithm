using System;
using System.Collections.Generic;

public class Solution 
{
    public int[] solution(int l, int r) 
    {
        List<int> answer = new List<int>{};
        
        for(int i = l; i <= r; i++)
        {
            string num = i.ToString();
            bool isValid = true;
            
            foreach(char c in num)
            {
                if(c != '0' && c != '5')
                {
                    isValid = false;
                    break;
                }
            }
            
            if(isValid)
            {
                answer.Add(i);
            }
            
        }
        
        if(answer.Count == 0)
        {
            answer.Add(-1);
        }
        
        return answer.ToArray();
    }
}