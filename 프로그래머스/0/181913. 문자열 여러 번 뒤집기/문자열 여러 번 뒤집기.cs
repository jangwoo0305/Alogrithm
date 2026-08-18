using System;

public class Solution {
    public string solution(string my_string, int[,] queries) 
    {
        char[] arr = my_string.ToCharArray();
        
        for(int k = 0; k < queries.GetLength(0); k++)
        {
            int s = queries[k,0];
            int e = queries[k,1];
            
            while(s < e)
            {
                char temp = arr[s];
                arr[s] = arr[e];
                arr[e] = temp;
                
                s++;
                e--;
            }
             
        }
        
        return new string(arr);
    }
}