using System;

public class Study
{
    public static void Main()
    {
        int N = int.Parse(Console.ReadLine());
        var studyTimes = new (int Start, int End)[N];
        
        for (int i = 0; i < N; i++)
        {
            string[] studyTime = Console.ReadLine().Split();
            studyTimes[i] = (int.Parse(studyTime[0]), int.Parse(studyTime[1]));
        }
        
        Array.Sort(studyTimes, (a, b) => a.End.CompareTo(b.End));

        // ---
        
        int lastEnd = 0;
        int Count = 0;

        for (int i = 0; i < N; i++)
        {
            if (studyTimes[i].Start >= lastEnd)
            {
                Count++;
                lastEnd = studyTimes[i].End;
            }
        }

        Console.WriteLine(Count);

    }
}