using System;

public class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        
        string ab = a.ToString() + b.ToString();
        
        int num1 = int.Parse(ab);
        int num2 = 2 * a * b;
        
        return num1 >= num2 ? num1 : num2;
    }
}