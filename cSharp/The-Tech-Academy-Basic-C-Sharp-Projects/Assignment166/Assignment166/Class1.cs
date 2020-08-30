using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Assignment166
{
    class Class1
    {
        public void Num1(int Number1, out int Number2)
        {
            Number1 *= 2;
            Number2 = 5;
            Console.WriteLine("The second value is " + Number2);
        }
    }
}
