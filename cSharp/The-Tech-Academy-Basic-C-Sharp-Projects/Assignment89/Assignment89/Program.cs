using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Assignment89
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Anonymous Income Comparison Program");
            Console.WriteLine("Please enter information for Person 1:");
            Console.WriteLine("Hourly Rate?");
            int p1Hourly = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Hours worked per week?");
            int p1Hours = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Please enter information for Person 2:");
            Console.WriteLine("Hourly Rate?");
            int p2Hourly = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Hours worked per week?");
            int p2Hours = Convert.ToInt32(Console.ReadLine());
            int p1annualHrs = p1Hours * 12;
            int p1Salary = p1Hourly * p1annualHrs;
            Console.WriteLine("Person 1's annual salary is: " + p1Salary);
            int p2annualHrs = p2Hours * 12;
            int p2Salary = p2Hourly * p2annualHrs;
            Console.WriteLine("Person 2's annual salary is: " + p2Salary);
            bool comPare = (p1Salary > p2Salary);
            Console.WriteLine(comPare);
            Console.ReadLine();
        }
    }
}
