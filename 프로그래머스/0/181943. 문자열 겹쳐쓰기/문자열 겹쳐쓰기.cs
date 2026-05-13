using System;

public class Solution {
    public string solution(string my_string, string overwrite_string, int s) 
    {
        string front = my_string.Substring(0, s);
        string behind = my_string.Substring(s + overwrite_string.Length);
        
        return front + overwrite_string + behind;
    }
}