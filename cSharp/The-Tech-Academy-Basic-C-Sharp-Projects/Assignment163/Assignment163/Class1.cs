using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Assignment163
{
    public class Numbers
    {
        public int Method1(int Number1, int Number2, out int Result1)
        {
            Number1 = 2;
            Number2 = 5;
            Result1 = Number1 * Number2;
            return Result1;
        }
        public decimal Method1(decimal Number3, decimal Number4, decimal Result2)
        {
            Number3 = 8.5m;
            Number4 = 2.5m;
            Result2 = (decimal)(Number3 + Number4);
            return Result2;
        }
        public string Method1(string Number5, string Number6, out string Result3)
        {
            Number5 = Console.ReadLine();
            Convert.ToInt32(Number5);
            Number6 = Console.ReadLine();
            Convert.ToInt32(Number6);
            Result3 = (Number5 + Number6);
            return Result3;
        }
    }
}
