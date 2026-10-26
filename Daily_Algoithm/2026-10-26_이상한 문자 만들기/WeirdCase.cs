using System;

public class Solution 
{
    public string solution(string s) 
    {
        string answer = "";
        string[] words = s.Split(' ');

        for (int i = 0; i < words.Length; i++)
        {
            string word = words[i];

            for (int j = 0; j < word.Length; j++)
            {
                if (j % 2 == 0)
                {
                    answer += char.ToUpper(word[j]);
                }
                else
                {
                    answer += char.ToLower(word[j]);
                }
            }
            if(i < words.Length - 1)
            {
                answer += " ";
            }
        }
        return answer;
    }
}

class Program
{
    static void Main()
    {
        string s = Console.ReadLine();

        Solution solution = new Solution();
        string result = solution.solution(s);

        Console.WriteLine(result);
    }
}