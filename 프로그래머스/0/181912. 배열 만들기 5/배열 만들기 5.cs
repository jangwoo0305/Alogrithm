using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(string[] intStrs, int k, int s, int l) 
    {
        List<int> answer = new List<int>();
        
        for(int i = 0; i < intStrs.Length; i++)
        {
            solution1(intStrs[i],k,s,l,answer);
        }
            
        return answer.ToArray();
    }
    
    // insStrs 조건 체크 후 조건이 충족 되면 list에 값을 넣어라
    public void solution1(string intStrs, int k, int s, int l, List<int> answer) 
    {
        string str = intStrs.Substring(s,l);
        int num = int.Parse(str);
        
        if (num > k)
        {
            answer.Add(num);
        }
    }
}