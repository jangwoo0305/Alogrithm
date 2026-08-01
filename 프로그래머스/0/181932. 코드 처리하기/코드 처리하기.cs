using System;

public class Solution {
    public string solution(string code) {
        string ret = "";
        int mode = 0;
        
        for (int idx = 0; idx < code.Length; idx++)
        {
            if(code[idx] == '1')
            {
                mode = 1 - mode;
            }
            else if(idx % 2 == mode)
            {
                ret += code[idx];
            }
        }
        return ret == "" ? "EMPTY" : ret;
    }
}