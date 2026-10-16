class AlternatingSignals
{
    public static void Main()
    {
        int n = int.Parse(Console.ReadLine()); // 신호의 개수
        string[] input = Console.ReadLine().Split(' ');
        int[] signal = new int[n];

        for (int i = 0; i < n; i++)
        {
            signal[i] = int.Parse(input[i]);
        }
        
        // --- 
        int currentLength = 1; // 현재 교대 구간의 길이
        int maxLength = 1;     // 가장 긴 교대 구간의 길이
        int startPosition = 1; // 가장 긴 교대 구간의 시작 위치

        // 배열을 순회하면서 교대 구간 찾기
        for (int i = 1; i < n; i++)
        {
            // 이전 숫자와 현재 숫자의 홀짝이 다른 경우
            if ((signal[i - 1] % 2 == 0) != (signal[i] % 2 == 0))
            {
                currentLength++;
            }
            else
            {
                // 교대가 끊어졌으므로 길이를 1로 초기화
                currentLength = 1;
            }
            // 지금까지의 최대 길이보다 길다면 갱신
            if (currentLength > maxLength)
            {
                maxLength = currentLength;

                // 현재 구간의 시작 위치 계산 (1부터 시작)
                startPosition = i - currentLength + 2;
            }
        }

        // 결과 출력
        Console.WriteLine($"{maxLength} {startPosition}");
    }
}
