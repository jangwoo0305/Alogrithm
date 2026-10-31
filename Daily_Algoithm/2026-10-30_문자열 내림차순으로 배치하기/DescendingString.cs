using System;

public class Solution 
{
    public string solution(string s) 
    {
        string answer = "";

        char[] answer_array = s.ToCharArray();
        Array.Sort(answer_array);
        Array.Reverse(answer_array);
        
        answer = new string(answer_array);
        return answer;
    }
}

public class Program
{
    public static void Main()
    {
        string s = Console.ReadLine();
        Solution solver = new Solution();

        Console.WriteLine(solver.solution(s));
    }
}