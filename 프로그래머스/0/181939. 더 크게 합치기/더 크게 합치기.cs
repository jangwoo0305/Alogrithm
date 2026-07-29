using System;

public class Solution {
    public int solution(int a, int b) 
    {
        int answer = 0;
        
        String a1 = a.ToString();
        String b1 = b.ToString();
        
        int a1b1 = int.Parse(a1 + b1);
        int b1a1 = int.Parse(b1 + a1);
        
        if(a1b1 >= b1a1)
            answer = a1b1;
        else
            answer = b1a1;
        
        return answer;
    }
}