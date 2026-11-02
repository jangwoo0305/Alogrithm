using System;
using System.Collections.Generic;

public class Solution
{
    public bool solution(string s)
    {
        bool answer = true;
        
        Stack<char> stack = new Stack<char>();

        for (int i = 0; i < s.Length; i++)
        {
            if (s[i] == '(')
            {
                stack.Push(s[i]);
            }
            else
            {
                if(stack.Count == 0)
                { 
                    answer = false;
                    break;
                }
                
                stack.Pop();
            }
        }

        if (stack.Count != 0)
        {
            answer = false;
        }
            
        return answer;
    }
}
class Program
{
    public static void Main()
    {
        Solution stackSolution = new Solution();
        Solution1 countSolution = new Solution1();
        string[] inputs = { "()()", "(())()", ")()(", "(()(" };

        foreach (string s in inputs)
        {
            Console.WriteLine("입력: " + s);
            Console.WriteLine("스택 풀이 결과: " + stackSolution.solution(s));
            Console.WriteLine("카운트 풀이 결과: " + countSolution.solution(s));
        }
    }
}
