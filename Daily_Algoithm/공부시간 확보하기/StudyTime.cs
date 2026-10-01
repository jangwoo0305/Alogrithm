using System;

public class StudyTime
{
    public static void Main()
    {
        // 첫번째 입력
        string[] firstInput = Console.ReadLine().Split();
        int n = int.Parse(firstInput[0]);
        int k = int.Parse(firstInput[1]);

        // 두번째 입력
        string[] secondInput = Console.ReadLine().Split();
        int[] times = new int[n];

        for (int i = 0; i < n; i++)
        {
            times[i] = int.Parse(secondInput[i]);
        }

        //---
        
		long sum = 0;
		int startDay = 1;

		for (int i = 0; i < k; i++)
		{
    		sum += times[i];
		}
		
		long maxSum = sum;

		for (int i = k; i < n; i++)
		{
    		sum = sum - times[i - k] + times[i];

    		if (sum > maxSum)
    		{
        		maxSum = sum;
        		startDay = i - k + 2;
    		}
		}

		Console.WriteLine($"{maxSum} {startDay}");

    }
}