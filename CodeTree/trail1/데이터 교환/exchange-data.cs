using System;

public class Codetree
{  
    public static void Main()
    {
        int a = 5, b = 6, c = 7;

        int temp = a;
        a = c;
        c = b;
        b = temp;

        Console.WriteLine(a);
        Console.WriteLine(b);
        Console.WriteLine(c);
    }
}
