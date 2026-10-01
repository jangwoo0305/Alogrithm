using System;

public class StudyTime
{
    public static void Main()
    {
        // 첫번째 입력
        string[] firstInput = Console.ReadLine().Split();
        int N = int.Parse(firstInput[0]);
        int K = int.Parse(firstInput[1]);

        // 두번째 입력
        string[] secondInput = Console.ReadLine().Split();
        int[] times = new int[N];

        for (int i = 0; i < N; i++)
        {
            times[i] = int.Parse(secondInput[i]);
        }

        //---
        
		long sum = 0;
		int startDay = 1;

		for (int i = 0; i < K; i++)
		{
    		sum += times[i];
		}

		// 첫 구간의 합을 초기 최대 합으로 저장
		long maxSum = sum;

		for (int i = K; i < N; i++)
		{
    		sum = sum - times[i - K] + times[i];

    		if (sum > maxSum)
    		{
        		maxSum = sum;
        		startDay = i - K + 2;
    		}
		}

		Console.WriteLine($"{maxSum} {startDay}");

    }
}