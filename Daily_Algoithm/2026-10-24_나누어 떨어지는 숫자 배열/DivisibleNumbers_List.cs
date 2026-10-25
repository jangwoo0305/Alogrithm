using System;
using System.Collections.Generic;

public class Solution1
{
    public int[] solution1(int[] arr, int divisor) {
        
        List<int> result = new List<int>();

        for (int i = 0; i < arr.Length; i++)
        {
            if (arr[i] % divisor == 0)
            {
                result.Add(arr[i]);
            }
        }

        if (result.Count == 0)
        {
            return new int[] { -1 };
        }
        
        int [] answer = result.ToArray();
        Array.Sort(answer);
        return answer;
    }
}