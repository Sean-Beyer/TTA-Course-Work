using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StringFunctions_Assingment125
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hi!");
            Console.WriteLine("What is your name?");
            string yourName = Console.ReadLine();
            string welCome = "Hello," + yourName + "\n \t I am very glad to meet you." + "\n \t \t What is the tempurature where you are at," + yourName + "?";
            Console.WriteLine(welCome);
            Console.ReadLine();

            int temp = Convert.ToInt32(Console.ReadLine());
            string tempInbox = "\t" + temp + "...huh. Probably is better than where I am at. \n\t\t You should really consider watercooling, " + yourName + "\n\t\t\t It really is more efficient.";
            Console.WriteLine(tempInbox + "\n\t\t\t\t How old are you" + yourName + "?");
            int age = Convert.ToInt32(Console.ReadLine());
            Console.ReadLine();

            string comMent = "Whew! " + age + "is old, \n\t at least from my point of view, \n\t\t but I am as old as when you bought me.";
            Console.WriteLine(comMent);
            Console.ReadLine();

            string toUp = "I noticed you like surfing the internet. That is cool.";
            toUp = toUp.ToUpper();
            Console.WriteLine(toUp);
            Console.ReadLine();

            StringBuilder statMent = new StringBuilder("Well, " + yourName + "\n\t it has been nice chatting with you. \n\t\t Maybe you should take a break. \n\t\t\t Hopefully I will get one soon but I don't need them as ofter as you.");
            Console.WriteLine(statMent);
            Console.ReadLine();
        }
    }
}
