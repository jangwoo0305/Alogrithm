using System;

public class Example
{
    public static void Main()
    {
        String str = Console.ReadLine();
        
        for (int i = 0; i < str.Length; i++)
        {
            if(Char.IsLower(str[i]))
            {
                Console.Write(char.ToUpper(str[i]));
            }
            else
            {
                Console.Write(char.ToLower(str[i]));
            }
        }       
    }
}