using System;

public class Solution {
    public string solution(string my_string, int s, int e)
    {
    
        char[] my_strings = new char[my_string.Length];
        
        int left = s;
        int right = e;
        char temp;
        
        for(int i = 0; i < my_string.Length; i++)
        {
            my_strings[i] = my_string[i];
        }
        
        while (left < right)
        {
            temp = my_strings[left];
            my_strings[left] = my_strings[right];
            my_strings[right] = temp;
            left++;
            right--;
        }
        
        string answer = new string(my_strings);
        
        return answer;
    }
}