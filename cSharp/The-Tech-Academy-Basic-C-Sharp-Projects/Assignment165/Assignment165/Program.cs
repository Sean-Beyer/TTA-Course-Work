using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Assignment165
{
    class Program
    {
        static void Main(string[] args)
        {
            Numbers numbers = new Numbers();

            int Number1 = 2;
            int Number2 = 5;

            Console.WriteLine("Enter a number.");
            int userNum1 = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Enter another number(Optional).");
            int userNum2 = Convert.ToInt32(Console.ReadLine());

            int getNumbers = userNum1;
            int getNumbers2 = numbers.Method1(Number1, Number2);

            Console.WriteLine("Your numbers are " + userNum1 + " and " + userNum2);
            Console.WriteLine("I wrote this maths here " + Number1 + " and will add in " + Number2 + " to equal ");

            Console.ReadLine();
        }
    }
}
