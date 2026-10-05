using System;
using System.Collections.Generic;

public class Observatory
{
    public static void Main()
    {
        int N  = int.Parse(Console.ReadLine());
        string[] Height = Console.ReadLine().Split();

        int[] result = new int[N];
        Stack<(int number, int Height)> stack = new Stack<(int number, int Height)>(); 

        // ---

        for (int i = 0; i < N; i++)
        {
            int currentHeight = int.Parse(Height[i]);

            while (stack.Count != 0 && stack.Peek().Height < currentHeight)
            {
                stack.Pop();
            }

            if (stack.Count == 0)
            {
                result[i] = 0;
            }
            else
            {
                result[i] = stack.Peek().number;
            }
            
            stack.Push((i+1, currentHeight));
        }
        
        Console.WriteLine(string.Join(" ", result));
    }
}