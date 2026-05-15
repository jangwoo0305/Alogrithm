using System;

public class Solution
{
    public int solution(int a, int b)
    {
        string ab = a.ToString() + b.ToString();
        int num_ab = int.Parse(ab);
        int num_2ab = 2*a*b;
        
        return num_ab > num_2ab ? num_ab : num_2ab;
    }
}