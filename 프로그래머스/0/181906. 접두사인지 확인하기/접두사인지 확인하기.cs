using System;

public class Solution {
    public int solution(string my_string, string is_prefix) 
    {
        int answer = 0;
        
        if(is_prefix.Length > my_string.Length)
        {
            answer = 0; 
        }
        else if(my_string.Substring(0,is_prefix.Length) == is_prefix)
        {
             answer = 1; 
        }
        
        return answer;
    }
}