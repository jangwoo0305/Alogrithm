using System;

public class Example
{
    public static void Main()
    {
        String[] str;
        str = Console.ReadLine().Split(" ");
        
        Console.WriteLine($"a = {str[0]}");
        Console.WriteLine($"b = {str[1]}");
    }
}