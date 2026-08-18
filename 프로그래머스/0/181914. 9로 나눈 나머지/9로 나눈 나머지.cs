using System;

public class Solution {
    public int solution(string number)
    {
        int answer = 0;
        
        for(int i = 0; i < number.Length; i++)
        {
            string digit = number[i].ToString();
            answer += int.Parse(digit);
            
        }
        
        return answer % 9;
    }
}