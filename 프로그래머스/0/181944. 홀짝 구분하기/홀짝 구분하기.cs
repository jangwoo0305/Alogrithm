using System;

public class Example
{
    public static void Main()
    {
        string s = Console.ReadLine();
        int n = int.Parse(s);
        
        if(n % 2 == 0)
            Console.WriteLine($"{n} is even");
        else
            Console.WriteLine($"{n} is odd");
    }
}