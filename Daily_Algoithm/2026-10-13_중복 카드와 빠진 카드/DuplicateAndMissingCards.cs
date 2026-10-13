class DuplicateAndMissingCards
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine()!);
        string[] input = Console.ReadLine().Split();
        int[] card_Number = new int[n];

        for (int i = 0; i < n; i++)
        {
            card_Number[i] = int.Parse(input[i]);
        }
        
        //--- 
        int[] check_Array = new int[n+1];

        for(int i = 0; i < card_Number.Length; i++)
        {
            check_Array[card_Number[i]]++;
        }
        
        int missingNumber = 0;
        int twiceNumber = 0;

        for (int number = 1; number <= n; number++)
        {
            if (check_Array[number] == 0)
                missingNumber = number;

            if (check_Array[number] == 2)
                twiceNumber = number;
        }

        Console.WriteLine($"{missingNumber} {twiceNumber}");
    }
}