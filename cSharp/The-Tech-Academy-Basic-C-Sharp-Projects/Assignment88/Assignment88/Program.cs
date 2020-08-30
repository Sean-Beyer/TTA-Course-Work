using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Assignment88
{
    class Program
    {
        static void Main()
        {
            Console.WriteLine("Enter a number.");
            string userNumber = Console.ReadLine();
            int userNum = Convert.ToInt32(userNumber);
            int total = userNum * 50;
            Console.WriteLine("The total is: " + total);
            Console.ReadLine();

            Console.WriteLine("Enter a number.");
            string userNumber2 = Console.ReadLine();
            int userNum2 = Convert.ToInt32(userNumber2);
            int total2 = userNum2 + 25;
            Console.WriteLine("The total is: " + total2);
            Console.ReadLine();

            Console.WriteLine("Enter a number.");
            string userNumber3 = Console.ReadLine();
            int userNum3 = Convert.ToInt32(userNumber3);
            double total3 = userNum3 / 12.5;
            Console.WriteLine("The total is: " + total3);
            Console.ReadLine();

            Console.WriteLine("Enter a number.");
            string userNum4 = Console.ReadLine();
            int userNumber4 = Convert.ToInt32(userNum4);
            int numBer = 50;
            bool trueOrFalse = userNumber4 > numBer;
            Console.WriteLine(trueOrFalse.ToString());
            Console.ReadLine();

            Console.WriteLine("Enter last number.");
            string userNum5 = Console.ReadLine();
            int userNumber5 = Convert.ToInt32(userNum5);
            int numBer2 = 7;
            int remainder = userNumber5 % numBer2;
            Console.WriteLine(remainder);
            Console.ReadLine();

            Console.WriteLine("All uR bAsE R belonG tO uS!");
            Console.ReadLine();
        }
    }
}
