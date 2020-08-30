using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Assignment190
{
    public class Employee<T> : Person//, //IQuittable
    {
        public List<T> Things { get; set; }
        public int ID { get; set; }

        //public override void SayName()
        //{
        //    Console.WriteLine("Name: " + FirstName + " " + LastName);
        //}

        //public void Quit()
        //{
        //    Console.WriteLine("I quit!");
        //}

        //public static bool operator !=(Employee employee1, Employee employee2)
        //{
        //    return employee1.ID != employee2.ID;
        //}

        //public static bool operator ==(Employee employee1, Employee employee2)
        //{
        //    return employee1.ID == employee2.ID;
        //}
    }
}
