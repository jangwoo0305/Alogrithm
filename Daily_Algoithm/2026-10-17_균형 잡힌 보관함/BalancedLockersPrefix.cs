class BalancedLockersPrefix
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
        
        //---
        
        long leftSum = 0;
        long rightSum = 0;
        int count = 0;
        int firstPos = 0;

        // 1번 보관함 선택
        for (int i = 1; i < n; i++)
        {
            rightSum += Locker[i];
        }
        
        // 1번 보관함 확인
        if (leftSum == rightSum)
        {
            count++;
            firstPos = 1;
        }
        
        // 2번 부터 선택 확인
        for (int i = 1; i < n; i++)
        {
            leftSum += Locker[i - 1];
            rightSum -= Locker[i];

            if (leftSum == rightSum)
            {
                count ++;
                
                if (firstPos == 0)
                {
                    firstPos = i + 1;
                }
            }
        }

    }
}