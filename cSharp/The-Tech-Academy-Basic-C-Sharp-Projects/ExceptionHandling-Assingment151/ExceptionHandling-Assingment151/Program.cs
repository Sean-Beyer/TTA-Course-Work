using System;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        List<int> ranDom = new List<int> { 2, 8, 10, 15, 20, 40, 50 };

        try
        {
            Console.WriteLine("Enter a number a number.");
            int numEntry = Convert.ToInt32(Console.ReadLine());

            foreach (int item in ranDom)
            {
                int numResult = item / numEntry;
                Console.WriteLine(numResult);
            }
        }
        catch (FormatException ex)
        {
            Console.WriteLine("Please enter a whole number.");
            return;
        }
        catch (DivideByZeroException ex)
        {
            Console.WriteLine("Please do not divide by zero.");
            return;
        }
        finally
        {
            Console.ReadLine();
        }
        Console.ReadLine();
    }
}

