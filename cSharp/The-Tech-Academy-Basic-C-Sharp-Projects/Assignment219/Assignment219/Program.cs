using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Assignment219
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Please enter a number: ");
            string text = Console.ReadLine();
            File.WriteAllText(@"C:\Users\Seann\Matrix\The-Tech-Academy-Basic-C-Sharp-Projects\Assignment219\number.txt", text);

            Console.WriteLine(File.ReadAllText(@"C:\Users\Seann\Matrix\The-Tech-Academy-Basic-C-Sharp-Projects\Assignment219\number.txt"));
            Console.ReadLine();
        }
    }
}
