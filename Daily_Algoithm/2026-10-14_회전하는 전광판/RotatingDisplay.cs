class RotatingDisplay
{
    static void Main()
    {
        //--- 입력
        string[] first = Console.ReadLine().Split();
        int n = int.Parse(first[0]); // 숫자의 개수
        int q = int.Parse(first[1]); // 명령의 개수
        
        string[] input = Console.ReadLine()!.Split();
        int[] numbers = new int[n];
        int start = 0;
        
        for (int i = 0; i < n; i++)
        {
            numbers[i] = int.Parse(input[i]);
        }

        for (int i = 0; i < q; i++)
        {
            string[] command = Console.ReadLine().Split();

            string text = command[0];
            char direction = text[0]; // 방향
            int k = int.Parse(command[1]); // 회전 횟수
            k = k % n;

            for (int count = 0; count < k; count++)
            {
                if (direction == 'L')
                {
                    int temp = numbers[0];

                    for (int j = 0; j < n - 1; j++)
                    {
                        numbers[j] = numbers[j + 1];
                    }
                    numbers[n-1] = temp;
                }
                else
                {
                    int temp = numbers[n - 1];
                    
                    for (int j = n - 1; j > 0; j--)
                    {
                        numbers[j] = numbers[j - 1];
                    }
                    numbers[0] = temp;
                }
            }
        }
        Console.WriteLine(string.Join(" ", numbers));
    }
}
