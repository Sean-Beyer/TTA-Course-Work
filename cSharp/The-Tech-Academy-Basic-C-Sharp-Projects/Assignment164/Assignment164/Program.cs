using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Assignment164
{
    class Program
    {
        static void Main(string[] args)
        {
            Numbers numbers = new Numbers();

            Console.WriteLine("Enter a number.");
            int userNum1 = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Enter another number(Optional).");
            string userNum2 = Console.ReadLine();

            int Number1 = 2;
            int GetResult1;

            if (userNum2 == "")
            {
                GetResult1 = numbers.Num1(userNum1);
            }
            else
            {
                GetResult1 = numbers.Num1(userNum1, Convert.ToInt32(userNum2));
            }

            Console.WriteLine("Those number(s) + 2 = " + GetResult1);
            Console.ReadLine();
        }
    }
}
