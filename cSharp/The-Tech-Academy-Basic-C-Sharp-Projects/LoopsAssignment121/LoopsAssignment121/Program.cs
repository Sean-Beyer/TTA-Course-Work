using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LoopsAssignment121
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Optimus Prime is the leader of which faction?");
            string leader = Console.ReadLine();
            bool gusSed = leader == "Autobots";

            while (!gusSed)
            {
                switch (leader)
                {
                    case "X-Men":
                        Console.WriteLine("You guessed X-Men. Try again.");
                        Console.WriteLine("Which faction?");
                        leader = Console.ReadLine();
                        break;
                    case "Power Rangers":
                        Console.WriteLine("You guessed Power Rangers. Try again.");
                        Console.WriteLine("Which faction?");
                        leader = Console.ReadLine();
                        break;
                    case "Justice League":
                        Console.WriteLine("You guessed Justice League. Try again.");
                        Console.WriteLine("Which faction?");
                        leader = Console.ReadLine();
                        break;
                    case "Autobots":
                        Console.WriteLine("You guessed Autobots. Good job, nerd!.");
                        gusSed = true;
                        break;
                    default:
                        Console.WriteLine("That's just wrong. Stick to sports...");
                        Console.WriteLine("Guess a Which faction?");
                        leader = Console.ReadLine();
                        break;
                }
            }
            Console.ReadLine();

            Console.WriteLine("How many teenage muntant ninja turtles are there?");
            int tmnt = Convert.ToInt32(Console.ReadLine());
            bool turtleGuess = tmnt == 4;

            do
            {
                switch (tmnt)
                {
                    case 8:
                        Console.WriteLine("You guessed 8. Try again.");
                        Console.WriteLine("Guess again?");
                        tmnt = Convert.ToInt32(Console.ReadLine());
                        break;
                    case 15:
                        Console.WriteLine("You guessed 15. Try again.");
                        Console.WriteLine("Guess again?");
                        tmnt = Convert.ToInt32(Console.ReadLine());
                        break;
                    case 2:
                        Console.WriteLine("You guessed 2. Try again.");
                        Console.WriteLine("Guess again?");
                        tmnt = Convert.ToInt32(Console.ReadLine());
                        break;
                    case 4:
                        Console.WriteLine("You guessed the number 4. Cowabunga!.");
                        turtleGuess = true;
                        break;
                    default:
                        Console.WriteLine("Totally not cool. Turtle soup anyone?");
                        Console.WriteLine("Again?");
                        tmnt = Convert.ToInt32(Console.ReadLine());
                        break;
                }
            }
            while (!turtleGuess);

            Console.ReadLine();
        }
    }
}
