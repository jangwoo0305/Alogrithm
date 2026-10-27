public class Solution 
{
    public bool solution(string s) 
    {
        bool answer = true;

        if (s.Length == 4 || s.Length == 6)
        {
            answer = true;
        }
        else
        {
            answer = false;
        }

        for (int i = 0; i < s.Length; i++)
        {
            if (!char.IsDigit(s[i]))
            {
                answer = false;
                break;
            }
        }
        
        return answer;
    }
}

class Program
{
    static void Main(string[] args)
    {
        string s = Console.ReadLine();
        Solution sol = new Solution();
        
        bool result = sol.solution(s);
        Console.WriteLine(result);
    }
}