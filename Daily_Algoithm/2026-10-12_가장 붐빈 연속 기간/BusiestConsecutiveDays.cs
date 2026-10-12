using System;

class BusiestConsecutiveDays
{
    public static void Main()
    {
        // --------- 입력
        string[] input = Console.ReadLine().Split();
        
        int N = int.Parse(input[0]);
        int K = int.Parse(input[1]);
        
        string[] parts = Console.ReadLine().Split();
        int[] visitors = new int[parts.Length];

        for (int i = 0; i < N; i++)
        {
            visitors[i] = int.Parse(parts[i]);
        }
        
        // --- 첫 K일의 합
        long curSum = 0;
        for (int i = 0; i < K; i++)
        {
            curSum += visitors[i];
        }
        long maxSum = curSum;
        
        // --- 하루씩 뒤로
        int startDay = 1;

        for (int i = K; i < N; i++)
        {
            curSum = curSum - visitors[i - K] + visitors[i];

            if (curSum > maxSum)
            {
                maxSum = curSum;
                startDay = i - K + 2;
            }
        }

        Console.WriteLine($"{startDay} {maxSum}");
    }
}