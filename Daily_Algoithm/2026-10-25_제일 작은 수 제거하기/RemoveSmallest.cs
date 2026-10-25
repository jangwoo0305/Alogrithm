using System;

public class Solution {
    public int[] solution(int[] arr)
    {
        
        if (arr.Length == 1)
        {
            return new int[] { -1 };
        }
        
        int[] answer = new int[arr.Length -1];
        
        int lowest = 0;
        
        for (int i = 0; i < arr.Length; i++)
        {
            if (arr[i] <  arr[lowest])
            {
                lowest = i;
            }
        }
        
        int index = 0;
        
        for (int j = 0; j < arr.Length; j++)
        {
            if (j == lowest)
            {
                continue;
            }

            answer[index] = arr[j];
            index++;
        }
        
        
        return answer;
    }
    
    
    public class Program
    {
        public static void Main()
        {
            int[] arr = { 4, 3, 2, 1 };

            Solution solution = new Solution();
            int[] result = solution.solution(arr);

            Console.WriteLine($"[{string.Join(", ", result)}]");
        }
    }
}