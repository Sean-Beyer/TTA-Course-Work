using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Assignment234
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("What is your age?");
            try
            {
                int age = Convert.ToInt32(Console.ReadLine());

                if (age < 0)
                {
                    throw new ArgumentException();
                }

                var today = DateTime.Today;
                var yob = today.Year - age;
                Console.WriteLine("You were born in " + yob);
            }
            catch (ArgumentException)
            {
                Console.WriteLine("Please enter positive numbers only.");    
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            Console.ReadLine();
        }
    }
}
