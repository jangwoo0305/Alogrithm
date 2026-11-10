using System;
using System.Collections.Generic;

public class Solution 
{
    public int solution(int bridge_length, int weight, int[] truck_weights)
    {
        int time = 0;
        int onBridgeWeight = 0; //다리에 올라와 있는 차들의 총 무게

        Queue<int> onBridgeCar = new Queue<int>(); // 다리에 올라와 있는 차를 담는 큐

        for (int i = 0; i < truck_weights.Length; i++)
        {
            while (true)
            {
                // 큐가 다리 길이만큼 차면 출구 쪽 값을 먼저 뺀다.
                if (onBridgeCar.Count == bridge_length)
                {
                    onBridgeWeight -= onBridgeCar.Dequeue();
                }

                if (onBridgeWeight + truck_weights[i] <= weight)
                {
                    onBridgeCar.Enqueue(truck_weights[i]);
                    onBridgeWeight += truck_weights[i];
                    time++;
                    break;
                }
                else
                {
                    // 이번 트럭이 못 들어가면 입구 쪽에 빈칸을 넣는다.
                    onBridgeCar.Enqueue(0);
                    time++;
                }
            }
        }

        // 마지막 트럭이 다리를 완전히 빠져나갈 때까지의 시간을 더한다.
        time += bridge_length;

        return time;
    }
}