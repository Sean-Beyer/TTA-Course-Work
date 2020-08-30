using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;

namespace Assignment200
{
    class Program
    {
        static void Main(string[] args)
        {
            Number num = new Number();
            num.Amount = 5.5m;

            Console.WriteLine(num.Amount);
            Console.ReadLine();
        }
    }
}
