using System;

public class Solution1
{
    public bool solution(string s)
    {
        bool answer = true;
        int left_cnt = 0;
        int right_cnt = 0;
    
        for (int i = 0; i < s.Length; i++)
        {
            if(s[i] == '(')
            {
                left_cnt++;
            }
            else
            {
                right_cnt++;
            }
        
            if(right_cnt > left_cnt)
            {
                answer = false;
            }
        
        }

        if (left_cnt != right_cnt)
        {
            answer = false;
        }

        return answer;
    }
}
