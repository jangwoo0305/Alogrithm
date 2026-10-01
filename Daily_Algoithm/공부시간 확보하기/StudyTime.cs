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
            times[i] = int.Parse(secondInput);
        }
        
        


    }
}