using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Assignment187
{
    class Program
    {
        static void Main(string[] args)
        {
            Employee emp1 = new Employee();
            emp1.FirstName = "Sample";
            emp1.LastName = "Student";
            emp1.ID = 1;

            Employee emp2 = new Employee();
            emp2.FirstName = "Example";
            emp2.LastName = "Pupil";
            emp2.ID = 2;
            
            emp1.SayName();

            IQuittable quittable = new Employee();
            quittable.Quit();

            Console.WriteLine(emp1.ID == emp2.ID);
            Console.ReadLine();
        }
    }
}
