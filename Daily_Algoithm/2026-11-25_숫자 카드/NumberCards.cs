using System;
using System.Collections.Generic;

public class NumberCards
{
    public static void Main()
    {
        int N  = int.Parse(Console.ReadLine());
        string[] input1 = Console.ReadLine().Split(' ');
        HashSet<int> havecards = new HashSet<int>(); 
 
        for (int i = 0; i < N; i++) 
        { 
            havecards.Add(int.Parse(input1[i])); 
        }
        
        int M = int.Parse(Console.ReadLine()); 
        string[] input2 = Console.ReadLine().Split(' '); 
        string[] answer = new string[M]; 

        for (int i = 0; i < M; i++) 
        { 
            int card = int.Parse(input2[i]); 
            answer[i] = havecards.Contains(card) ? "1" : "0"; 
        } 

        Console.WriteLine(string.Join(" ", answer));
    }
}