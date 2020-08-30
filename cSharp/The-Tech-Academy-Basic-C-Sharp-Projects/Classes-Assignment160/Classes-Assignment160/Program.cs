using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;

namespace Classes_Assignment160
{
    class Program
    {
        static void Main(string[] args)
        {
            Numbers numbers = new Numbers();

            Console.WriteLine("Enter a number.");
            int userNum = Convert.ToInt32(Console.ReadLine());

            int Number1 = 2;
            int Number2 = 5;
            int Number3 = 10;


            int result1 = numbers.Num1(userNum, Number1);
            int result2 = numbers.Num2(userNum, Number2);
            int result3 = numbers.Num3(userNum, Number3);

            Console.WriteLine("Your number + 2 = " + result1);
            Console.WriteLine("Your number + 5 = " + result2);
            Console.WriteLine("Your number + 10 = " + result3);
            Console.ReadLine();
        }
    }
}
