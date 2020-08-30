using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Assignment190
{
    class Program
    {
        static void Main(string[] args)
        {
            Employee<string> employee = new Employee<string>();
            employee.Things = new List<string>();
            employee.Things.Add("Sean");
            employee.Things.Add("Megan");

            foreach (var thing in employee.Things)
            {
                Console.WriteLine("Here are some things: " + thing);
            }

            Employee<int> empNumbers = new Employee<int>();
            empNumbers.Things = new List<int>() { 2, 4, 6, 8, 10 };

            foreach (var thing in empNumbers.Things)
            {
                Console.WriteLine("Here are some other things: " + thing);
            }
            Console.ReadLine();

            //Employee emp1 = new Employee();
            //emp1.FirstName = "Sample";
            //emp1.LastName = "Student";
            //emp1.ID = 1;

            //Employee emp2 = new Employee();
            //emp2.FirstName = "Example";
            //emp2.LastName = "Pupil";
            //emp2.ID = 2;

            //emp1.SayName();

            //IQuittable quittable = new Employee();
            //quittable.Quit();

            //Console.WriteLine(emp1.ID == emp2.ID);
            //Console.ReadLine();
        }
    }
}
