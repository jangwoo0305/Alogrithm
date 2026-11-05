using System;
using System.Collections.Generic;

public class Solution 
{
    public int[] solution(int[] progresses, int[] speeds) 
    {
        List<int> workdays = new List<int>();
        List<int> result = new List<int>();
        
        for (int i = 0; i < progresses.Length; i++)
        {
            int remain_Work = 100 - progresses[i];
            int remain_Workday = remain_Work / speeds[i];

            if (remain_Work % speeds[i] != 0)
            {
                remain_Workday += 1;
            }

            workdays.Add(remain_Workday);
        }

        int releaseDay = workdays[0]; 
        int count = 1;             

        for (int i = 1; i < workdays.Count; i++)
        {
            if (workdays[i] <= releaseDay)
            {
                count++;
            }
            else
            {
                result.Add(count);   
                releaseDay = workdays[i];
                count = 1;               
            }
        }

        result.Add(count);
        
        return result.ToArray();
    }
}