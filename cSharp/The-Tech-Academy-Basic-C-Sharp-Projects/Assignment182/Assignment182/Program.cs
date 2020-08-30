using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Assignment182
{
    class Program
    {
        static void Main(string[] args)
        {
            Employee emp1 = new Employee();
            emp1.FirstName = "Sample";
            emp1.LastName = "Student";
            emp1.SayName();

            IQuittable quittable = new Employee();
            quittable.Quit();
            Console.ReadLine();
        }
    }
}
