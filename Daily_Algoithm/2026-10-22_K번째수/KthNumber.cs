using System;

public class Solution 
{
    public int[] solution(int[] array, int[,] commands)
    {
        int[] answer = new int[commands.GetLength(0)];

        for (int row = 0; row < commands.GetLength(0); row++)
        {
            int i = commands[row, 0];
            int j = commands[row, 1];
            int k = commands[row, 2];
            
            int[] temp = new int[j - i + 1];

            for (int cnt = i - 1; cnt < j; cnt++)
            {
                temp[cnt - (i - 1)] = array[cnt];
                
            }
            Array.Sort(temp);
            answer[row] = temp[k - 1];
        }
        return answer;
    }
}

class Program
{
    static void Main()
    {
        int[] array = { 1, 5, 2, 6, 3, 7, 4 };
        int[,] commands =
        {
            { 2, 5, 3 },
            { 4, 4, 1 },
            { 1, 7, 3 }
        };

        Solution sol = new Solution();
        int[] result = sol.solution(array, commands);

        foreach (int number in result)
        {
            Console.WriteLine(number);
        }
    }
}