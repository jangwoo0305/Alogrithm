using System;
using System.Collections.Generic;

public class Solution1
{
    public int[] solution(int[] numbers)
    {
        List<int> answer = new List<int>();

        for (int i = 0; i < numbers.Length; i++)
        {
            for (int j = i + 1; j < numbers.Length; j++)
            {
                int pairSums = numbers[i] + numbers[j];

                if (!answer.Contains(pairSums))
                {
                    answer.Add(pairSums);
                }
            }
        }

        answer.Sort();

        return answer.ToArray();
    }
}