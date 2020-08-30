using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Branching
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("What is your favorite number?");
            int favNum = Convert.ToInt32(Console.ReadLine());

            string result = favNum == 12 ? "you have an awesome favorite number." : "You do not have an awesome favorite number.";

            Console.WriteLine(result);
            Console.ReadLine();


            //int roomTempurature = 70;

            //Console.WriteLine("Hi, what is your name?");
            //string name = Console.ReadLine();

            //Console.WriteLine("Hi, " + name + ", what is the tempurature where you are?");
            //int currentTempurature = Convert.ToInt32(Console.ReadLine());

            //if (currentTempurature == roomTempurature)
            //{
            //    Console.WriteLine("It is exactly room tempurature.");
            //}
            //else if (currentTempurature > roomTempurature)
            //{
            //    Console.WriteLine("It is warmer than room tempurature.");
            //}
            //else if (roomTempurature > currentTempurature)
            //{
            //    Console.WriteLine("It is colder than room tempurature.");
            //}
            //else
            //{
            //    Console.WriteLine("uhhhh..... something went wront.");
            //}

            //Console.ReadLine();

            //int currentTempurature = 80;
            //int roomTempurature = 70;

            //string comparisonResult = currentTempurature == roomTempurature ? "It is room temp." : "It is not room temp.";

            //Console.WriteLine(comparisonResult);
            //Console.ReadLine();


            //if (currentTempurature == roomTempurature)
            //{
            //    Console.WriteLine("It is exactly room tempurature.");
            //}
            //else if (currentTempurature > roomTempurature)
            //{
            //    Console.WriteLine("It is warmer than room tempurature.");
            //}
            //else if (roomTempurature > currentTempurature)
            //{
            //    Console.WriteLine("Room tempurature is warmer than current tempurature.");
            //}
            //else
            //{
            //    Console.WriteLine("It's not exactly room tempurature.");
            //}
            //Console.ReadLine();
        }
    }
}
