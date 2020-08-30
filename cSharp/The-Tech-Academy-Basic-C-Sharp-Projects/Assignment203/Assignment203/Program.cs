using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;

namespace Assignment203
{
    class Program
    {
        static void Main(string[] args)
        {
            List<Employees> employees = new List<Employees>{
            new Employees{ FirstName = "Sean", LastName = "Beyer", ID = 1 },
            new Employees{ FirstName = "Megan", LastName = "Beyer", ID = 2 },
            new Employees{ FirstName = "Chicka", LastName = "Walker", ID = 3 },
            new Employees{ FirstName = "Justin", LastName = "Walker", ID = 4 },
            new Employees{ FirstName = "Joe", LastName = "Hagen", ID = 5 },
            new Employees{ FirstName = "Michael", LastName = "Meacham", ID = 6 },
            new Employees{ FirstName = "Liesha", LastName = "Meacham", ID = 7 },
            new Employees{ FirstName = "Brandon", LastName = "McClosky", ID = 8 },
            new Employees{ FirstName = "Andrew", LastName = "Mondor", ID = 9 },
            new Employees{ FirstName = "Joe", LastName = "Jessup", ID = 10 },
            };

            List<Employees> JoeList = new List<Employees>();
            foreach (Employees employee in employees)
            {
                if (employee.FirstName == "Joe")
                {
                    JoeList.Add(employee);
                    Console.WriteLine(employee.FirstName + " " + employee.LastName);
                }
            }
            foreach(Employees joeEntry in JoeList)
            {
                Console.WriteLine(joeEntry.FirstName + " " + joeEntry.LastName);
            }
            Console.ReadLine();

            List<Employees> AllJoe = new List<Employees>();
            AllJoe = employees.FindAll(e => e.FirstName == "Joe").ToList();
            foreach (Employees joeEntry in AllJoe)
            {
                Console.WriteLine(joeEntry.FirstName + " " + joeEntry.LastName);
            }
            Console.ReadLine();

            List<Employees> BigNumber = new List<Employees>();
            BigNumber = employees.FindAll(e => e.ID >= 5).ToList();
            foreach (Employees Five in BigNumber)
            {
                Console.WriteLine(Five.FirstName + " " + Five.LastName);
            }
            Console.ReadLine();
        }
    }
}
