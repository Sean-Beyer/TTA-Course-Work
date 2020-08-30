using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Assignment169
{
    class Program
    {
        static void Main(string[] args)
        {
            Class1 numbers = new Class1();

            Console.WriteLine("Enter a number.");
            int userNum = Convert.ToInt32(Console.ReadLine());

            numbers.Num1(out int Number1);
            int result1 = userNum / Number1;

            Console.WriteLine("Your number divided by 2 equals " + result1);
            Console.ReadLine();
        }
    }
}
