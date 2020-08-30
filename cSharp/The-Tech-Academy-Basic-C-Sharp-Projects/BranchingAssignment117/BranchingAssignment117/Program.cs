using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BranchingAssignment117
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Welcome to Package Express. Please follow the instructions below.");

            Console.WriteLine("Please enter the weight of your package:");
            int packWeight = Convert.ToInt32(Console.ReadLine());
            int shipWeight = 50;

            if (packWeight >= shipWeight)
            {
                Console.WriteLine("Package too heavy to be shipped via Package Express. Have a good day.");
                Console.ReadLine();
            }
            else
            {
                Console.WriteLine("Thanks! Please continue.");
                Console.ReadLine();

                Console.WriteLine("Now, please enter the width of your package:");
                int packWidth = Convert.ToInt32(Console.ReadLine());

                Console.WriteLine("Then, please enter the height of your package:");
                int packHeight = Convert.ToInt32(Console.ReadLine());

                Console.WriteLine("Finally, please enter the length of your package:");
                int packLength = Convert.ToInt32(Console.ReadLine());
                Console.WriteLine("Thank you. One moment please.");
                Console.ReadLine();

                int packSize = (packWidth + packHeight + packLength);

                if (packSize >= 50)
                {
                    Console.WriteLine("Package too big to be shipped via Package Express. Have a good day.");
                    Console.ReadLine();
                }
                else
                {
                    int shipDimensions = packWidth * packHeight * packLength;
                    int shipPackage = shipDimensions * packWeight;
                    double shipCharge = shipPackage / 100.00;

                    Console.WriteLine("Your estimated total for shipping this package is: $" + shipCharge);
                    Console.ReadLine();
                    
                    Console.WriteLine("Payment is to be paid immediately or you will suffer...");
                    Console.WriteLine("Thank you, have a good day!");
                    Console.ReadLine();
                }
            }
        }
    }
}
