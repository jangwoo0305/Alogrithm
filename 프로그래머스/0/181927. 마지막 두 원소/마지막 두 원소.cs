using System;

public class Solution {
    public int[] solution(int[] num_list) 
    {
        int[] answer = new int[num_list.Length + 1];
        
        
        for (int idx = 0; idx < num_list.Length; idx++)
        {
            answer[idx] = num_list[idx];
        }
        
        int last = num_list[num_list.Length - 1];
        int beforelast = num_list[num_list.Length - 2];
        
        if (last > beforelast)
        {
            answer[answer.Length - 1] = last - beforelast;
        }
        else
        {
            answer[answer.Length - 1] = last*2;
        }
            
        return answer;
    }
}