using System;
using System.Collections.Generic;

public class RobotShortestPath
{
    public static void Main()
    {
        string[] size = Console.ReadLine().Split();
        
        int R = int.Parse(size[0]);
        int C = int.Parse(size[1]);
        
        char [][] map =  new char[R][];

        for (int row = 0; row < R; row++)
        {
            char[] line = Console.ReadLine().ToCharArray();
            map[row] = line;
        }
        
        // ---

        int startRow = -1;
        int startCol = -1;
        int goalRow = -1;
        int goalCol = -1;

        for (int row = 0; row < R; row++)
        {
            for (int col = 0; col < C; col++)
            {
                if (map[row][col] == 'S')
                {
                    startRow = row;
                    startCol = col;
                }
                else if (map[row][col] == 'G')
                {
                    goalRow = row;
                    goalCol = col;
                }
            }
        }
        int[,] distances = new int[R,C];

        for (int row = 0; row < R; row++)
        {
            for (int col = 0; col < C; col++)
            {
                distances[row, col] = -1;
            }
        }

        Queue<(int row,int col)> queue = new Queue<(int row, int col)>();
        distances[startRow, startCol] = 0;
        queue.Enqueue((startRow, startCol));
        
        int[] deltaRow = { -1, 1, 0, 0 };
        int[] deltaCol = { 0, 0, -1, 1 };
        
        while (queue.Count > 0)
        {
            var current = queue.Dequeue();

            for (int i = 0; i < 4; i++)
            {
                int nextRow = current.row + deltaRow[i];
                int nextCol = current.col + deltaCol[i];

                if (nextRow < 0 || nextRow >= R || nextCol < 0 || nextCol >= C)
                {
                    continue;
                }

                if (map[nextRow][nextCol] == '#')
                {
                    continue;
                }

                if (distances[nextRow, nextCol] != -1)
                {
                    continue;
                }

                distances[nextRow, nextCol] = distances[current.row, current.col] + 1;
                queue.Enqueue((nextRow, nextCol));
            }
        }
        
        Console.WriteLine(distances[goalRow, goalCol]);
    }
}