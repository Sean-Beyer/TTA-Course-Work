using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Assignment163
{
    class Program
    {
        static void Main(string[] args)
        {
            Numbers number = new Numbers();

            int Number1 = 2;
            int Number2 = 5;
            int Result1 = Number1 * Number2;
            int GetResult1 = number.Method1(Number1, Number2, out Result1);

            Console.WriteLine(GetResult1);
            Console.ReadLine();

            decimal Number3 = 8.5m;
            decimal Number4 = 2.5m;
            decimal Result2 = (decimal)((decimal)Number3 + Number4);
            decimal GetResult2 = number.Method1((decimal)Number3, (decimal)Number4, (decimal)Result2);

            Console.WriteLine(GetResult2);
            Console.ReadLine();

            Console.WriteLine("Enter a number:");
            int Number5 = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Enter another number:");
            int Number6 = Convert.ToInt32(Console.ReadLine());
            Convert.ToInt32(Number6);
            int Result3 = (int)(Number5 + Number6);
            int GetResult3 = number.Method1((int)Number5, (int)Number6, out Result3);

            Console.WriteLine(GetResult3);
            Console.ReadLine();
        }
    }
}
