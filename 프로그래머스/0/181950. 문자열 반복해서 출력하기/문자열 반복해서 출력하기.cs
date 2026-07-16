using System;

public class Example
{
    public static void Main()
    {
        String[] str;
        String Answer = "";
        
        str = Console.ReadLine().Split(" "); // [string,5]
        int n = int.Parse(str[1]);
        
        for(int i = 0; i < n; i++)
        {
            Answer += str[0];
        }
        
        Console.WriteLine(Answer);
        
    }
}