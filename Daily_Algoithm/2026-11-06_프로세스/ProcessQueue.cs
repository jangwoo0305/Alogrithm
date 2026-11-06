using System;
using System.Collections.Generic;

public class Solution 
{
    public int solution(int[] priorities, int location) 
    {
        Queue<(int idx, int priority)> process = new Queue<(int, int)>();
        int answer = 0;
        
        for(int i = 0; i < priorities.Length; i++)
        {
            process.Enqueue((i, priorities[i]));
        }
        
        while (process.Count > 0)
        {
            var current = process.Dequeue();
            bool hasHigherPriority = false;

            // 남아 있는 프로세스 중
            // current.priority보다 우선순위가 높은 것이 있는지 확인

            foreach (var p in process)
            {
                if (p.priority > current.priority)
                {
                    hasHigherPriority = true;
                    break;
                }
            }
            
            if (hasHigherPriority)
            {
                process.Enqueue(current);
            }
            else
            {
                // 더 높은 우선순위가 없으면 실행
                answer++;

                // 실행한 프로세스가 찾던 프로세스라면 실행 순서 반환
                if (current.idx == location)
                {
                    return answer;
                }
            }
        }
        return answer;
    }
}