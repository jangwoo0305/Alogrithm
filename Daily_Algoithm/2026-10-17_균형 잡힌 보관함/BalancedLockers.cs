class BalancedLockers
{
    public static void Solve()
    {
        int n = int.Parse(Console.ReadLine());
        string[] input  = Console.ReadLine().Split(' ');
        int[] Locker = new int[n];
        for (int i = 0; i < n; i++)
        {
            Locker[i] = int.Parse(input[i]);
        }

        int count = 0; // 균형 위치 개수
        int startposition = 0; // 가장 왼쪽 균형 위치의 번호
        
        for (int i = 0; i < n; i++)
        {
            long leftSum = 0;
            long rightSum = 0;
            
            for(int j = 0; j < i; j++)
            {
                leftSum += Locker[j];
            }
            for(int j = i + 1; j < n; j++)
            {
                rightSum += Locker[j];
            }

            if (leftSum == rightSum)
            {
                count++;

                if (startposition == 0)
                {
                    startposition = i + 1;
                }
            }
        }
        Console.WriteLine($"{count} {startposition}");
    }
}