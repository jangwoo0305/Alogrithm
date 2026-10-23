using System;

public class Solution {
    public int[] solution(int[] numbers) {
        
        int size = 0;

        for (int i = 0; i < numbers.Length; i++)
        {
            for (int j = i + 1; j < numbers.Length; j++)
            {
                size++;
            }
        }

        int[] answer = new int[size];
        int index = 0;
        
        for (int i = 0; i < numbers.Length; i++)
        {
            int select_num =  numbers[i];

            for (int j = i + 1; j < numbers.Length; j++)
            {
                int pairSums = select_num + numbers[j];
                
                bool isDuplicate = false;

                for (int k = 0; k < index; k++)
                {
                    if (answer[k] == pairSums)
                    {
                        isDuplicate = true;
                        break;
                    }
                }

                if (isDuplicate == false)
                {
                    answer[index] = pairSums;
                    index++;
                }
            }
        }
        
        Array.Resize(ref answer, index);
        Array.Sort(answer);

        return answer;
    }
}

class Program
{
    public static void Main()
    {
        Solution sol = new Solution();
        int[] numbers = { 2, 1, 3, 4, 1 };
        int[] result = sol.solution(numbers);
        Console.WriteLine("결과: " + string.Join(", ", result));
    }
}