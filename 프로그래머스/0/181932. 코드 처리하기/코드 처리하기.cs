using System;

public class Solution {
    public string solution(string code) {
        string ret = "";
        int mode = 0;
        
        for(int i = 0; i < code.Length; i++)
        {
            if (mode == 0)
            {
                if(code[i] != '1')
                {
                    if(i % 2 == 0)
                    {
                        ret += code[i];
                    }
                }
                else
                {
                    mode = 1;
                }
            }
            else
            {
                if(code[i] != '1')
                {
                    if(i % 2 != 0)
                        ret += code[i];
                }
                else
                {
                    mode =  0;
                }
            }
        }
                
        if (ret == "")
            return "EMPTY";
        
        return ret;
    }
}