using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Assignment195
{
    [Flags] enum DaysOfTheWeek { Monday, Tuesday, Wednseday, Thursday, Friday, Saturday, Sunday };

    public class Example
    {
        public static void Main()
        {   
            Console.WriteLine("What day is it?");
            string selection = Console.ReadLine();

            try
            {
                DaysOfTheWeek enumSelection = (DaysOfTheWeek)Enum.Parse(typeof(DaysOfTheWeek), selection, true);
                Console.WriteLine("'{0}' Ah, hope it's a good one for you.", enumSelection, selection.ToString());
            }
            catch (ArgumentException)
            {
                Console.WriteLine("Please enter an actual day of the week.", selection);
            }
            Console.ReadLine();
        }
    }
}
