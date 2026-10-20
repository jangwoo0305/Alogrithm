class SingleVisitGuests
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string[] input = Console.ReadLine().Split(' ');
        int[] visiters = new int[n];
        for (int i = 0; i < n; i++)
        {
            visiters[i] = int.Parse(input[i]);
        }
        
        // ---

        int visitOnce = 0;
        int firstGuest = 0;
        int [] count = new int[100001];

        for (int i = 0; i < visiters.Length; i++)
        {
            int num = visiters[i];
            count[num]++;
        }

        for (int i = 0; i < visiters.Length; i++)
        {
            int num = visiters[i];
            
            if (count[num] == 1)
            {
                visitOnce++;
                
                if (firstGuest == 0)
                {
                    firstGuest = visiters[i];
                }
            }
        }
        Console.WriteLine($"{visitOnce} {firstGuest}");
    }
}