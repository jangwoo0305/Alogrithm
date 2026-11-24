using System;
using System.Collections.Generic;

public class StringSet
{
    public static void Main()
    {
        string[] input = Console.ReadLine().Split(' ');
        int N = int.Parse(input[0]);
        int M = int.Parse(input[1]);

        HashSet<string> stringSet = new HashSet<string>();
        int cnt = 0;
        
        
        for (int i = 0; i < N; i++)
        {
            string includeString = Console.ReadLine();
            stringSet.Add(includeString);
        }
        for (int i = 0; i < M; i++)
        {
            string checkString = Console.ReadLine();

            if (stringSet.Contains(checkString))
            {
                cnt++;
            }
        }
        
        Console.WriteLine(cnt);
    }
}