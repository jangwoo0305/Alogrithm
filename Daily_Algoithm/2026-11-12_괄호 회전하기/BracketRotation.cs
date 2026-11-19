using System;
using System.Collections.Generic;

public class Solution 
{
    public int solution(string s) 
    {
        
        Queue<char> queue = new Queue<char>(); // 회전을 시키기 위함
        Stack<char> stack = new Stack<char>(); // 괄호가 정상적으로 닫혔는지 확인하기 위함
        int answer = 0;

        foreach (char c in s)
        {
            queue.Enqueue(c);
        }

        for (int i = 0; i < queue.Count; i++)
        {
            bool isValid = true;
            
            foreach (char c in queue)
            {
                if (c == '(' || c == '[' || c == '{')
                {
                    stack.Push(c);
                }
                else
                {
                    if (stack.Count == 0)
                    {
                        isValid = false;
                        break;
                    }
                    else
                    {
                        char open = stack.Pop();
                        if ((open == '(' && c != ')') ||
                            (open == '[' && c != ']') ||
                            (open == '{' && c != '}'))
                        {
                            isValid = false;
                            break;
                        }
                    }
                    
                }
            }
            
            if (isValid && stack.Count == 0)
            {
                answer++;
            }
            // 괄호 검사 로직 
            char front_char = queue.Dequeue();
            queue.Enqueue(front_char);
        }
        
        return answer;
    }
}