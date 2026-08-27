using System;

public class Solution {
    public string solution(string[] my_strings, int[,] parts)
    {
        string answer = "";
        
        for(int i = 0; i < parts.GetLength(0); i++)
        {
            int s = parts[i,0];
            int e = parts[i,1];
            
            string str = my_strings[i];
            
            answer += str.Substring(s, e - s + 1);
        }
        
        return answer;
    }
}