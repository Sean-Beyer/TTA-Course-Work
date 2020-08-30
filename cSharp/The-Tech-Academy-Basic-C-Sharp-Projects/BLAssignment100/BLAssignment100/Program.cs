using System;


namespace BLAssignment100
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("DMV Recode");
            Console.WriteLine("Qualification for Car Insurence");
            Console.ReadLine();

            Console.WriteLine("What is your age?");
            int yourAge = Convert.ToInt32(Console.ReadLine()); //converts age string to intager

            Console.WriteLine("Have you ever had a DUI?");
            bool anyDuis = (true || false);
            Console.ReadLine(); //bool values asks true or false statement

            Console.WriteLine("How many speeding tickets do you have?");
            int speedTickets = Convert.ToInt32(Console.ReadLine()); //converts number of tickets from string to intager

            bool quaLified = yourAge >= 15 && anyDuis == false && speedTickets <= 3; //evalueates questions
            Console.WriteLine("Are you qualified?");
            Console.WriteLine(quaLified); //will produce true or false value to verify if user is qualified

            Console.ReadLine();
        }
    }
}
