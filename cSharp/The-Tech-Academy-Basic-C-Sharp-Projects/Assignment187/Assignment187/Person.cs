using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Assignment187
{
    public abstract class Person
    {
        public List<string> Employees { get; set; }
        public string FirstName { get; set; }
        public string LastName { get; set; }

        public abstract void SayName();

        
    }
}
