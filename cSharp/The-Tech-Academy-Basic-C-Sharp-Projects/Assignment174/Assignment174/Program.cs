﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Assignment174
{
    class Program
    {
        static void Main(string[] args)
        {
            Employee emp1 = new Employee();
            emp1.FirstName = "Sample";
            emp1.LastName = "Student";
            emp1.SayName();
            Console.ReadLine();
        }
    }
}
