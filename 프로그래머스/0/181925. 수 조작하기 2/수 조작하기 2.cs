using System;

public class Solution 
{
    public string solution(int[] numLog)
    {
        string answer = "";
        
        for(int i = 0; i < numLog.Length - 1; i++)
        {
            int diff = numLog[i+1] - numLog[i];
            
            if (diff == 1)
                answer += "w";
            else if(diff == -1)
                answer += "s";
            else if(diff == 10)
                answer += "d";
            else
                answer += "a";
        }
        
        return answer;
    }
}