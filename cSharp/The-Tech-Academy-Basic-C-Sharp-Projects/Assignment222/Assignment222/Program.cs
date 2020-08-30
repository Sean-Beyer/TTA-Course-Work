using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Assignment222
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Please enter a number: ");
            int number = Convert.ToInt32(Console.ReadLine());
            DateTime current = DateTime.Now;
            var futuretime = current.AddHours(number);
            Console.WriteLine("In " + number + " hours, it will be " + futuretime + ".");
            Console.ReadLine();
        }
    }
}
