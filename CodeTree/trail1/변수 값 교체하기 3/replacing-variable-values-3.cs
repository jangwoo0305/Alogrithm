using System;

public class Codetree
{  
    public static void Main()
    {
        int a = 3, b = 5;

        int temp = a;
        a = b;
        b = temp;

        Console.WriteLine(a);
        Console.WriteLine(b);
    }
}
