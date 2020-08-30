using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Assignment230
{
    public class simpleNumber
    {
        public int Number { get; set; }
        public simpleNumber() : this(10)
        { 
        }

        public simpleNumber(int number)
        {
            Number = number;
        }
    }

}
