using System;
using System.Collections.Generic;

namespace ArrayAndLists_Assignment130
{
    class Program
    {
        static void Main()
        {
            // String
            string[] rangers = new string[] { "Jason - Red Ranger", "Trini - Yellow Ranger", "Billy - Blue Ranger", "Zack - Black Ranger", "Kimberly - Pink Ranger", "Tommy - Green Ranger" };
            
            Console.WriteLine("Who is your favorite Power Ranger?");
            Console.WriteLine("1-6?");
            int pickRangers = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Your favorite is: " + rangers[pickRangers]);
            Console.ReadLine();

            // Intagers
            int[] answer = new int[] { 7, 13, 42, 69, 420 };

            Console.WriteLine("What is the answer to life, the universe and everything?");
            int theAnswer = Convert.ToInt32(Console.ReadLine());
            Console.ReadLine();
            bool correctAnswer = theAnswer == 42;

            while (!correctAnswer)
            {
                switch (theAnswer)
                {
                    case 7:
                        Console.WriteLine("You guessed 7. You're not at a casino.");
                        Console.WriteLine("Try again.");
                        theAnswer = Convert.ToInt32(Console.ReadLine());
                        break;
                    case 13:
                        Console.WriteLine("You guessed 13. Superstitious, are we?");
                        Console.WriteLine("Try again.");
                        theAnswer = Convert.ToInt32(Console.ReadLine());
                        break;
                    case 42:
                        Console.WriteLine("So long and thanks for all the fish!");
                        correctAnswer = true;
                        break;
                    case 69:
                        Console.WriteLine("You guessed 69. Just, get out...");
                        Console.WriteLine("Try again.");
                        theAnswer = Convert.ToInt32(Console.ReadLine());
                        break;
                    case 420:
                        Console.WriteLine("You guessed 420. No way, man...");
                        Console.WriteLine("Try again.");
                        theAnswer = Convert.ToInt32(Console.ReadLine());
                        break;
                    default:
                        Console.WriteLine("Negative, Ghost Rider");
                        Console.WriteLine("Try again.");
                        theAnswer = Convert.ToInt32(Console.ReadLine());
                        break;
                }
            }
            Console.ReadLine();
        }
    }
}
