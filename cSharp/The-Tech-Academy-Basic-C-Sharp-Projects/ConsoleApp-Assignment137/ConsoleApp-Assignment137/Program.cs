using System;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        // Original part 1
        string[] leaders = { "Optimus Prime", "Leonardo", "Kirk", "Jason" };

        Console.WriteLine("Add the name of a leader of a fantasy group.");
        string addedName = Console.ReadLine();

        for (int l = 0; l < leaders.Length; l++)
        {
            Console.WriteLine(leaders[l] + " " + addedName);
        }
        Console.ReadLine();

        //Part 2 - 5
        for (int l = 10; l > leaders.Length; l++)
        {
            Console.WriteLine(leaders);
            break;
        }
        Console.ReadLine();

        // Part 6
        List<string> faVs = new List<string>() { "Amplitude", "City of Heroes", "Star Trek Online", "Starfinder" };

        Console.WriteLine("A few of my favorite games.");
        Console.WriteLine(""); // whitespace

        Console.WriteLine("Select a title.");
        string favSearch = Console.ReadLine();

        foreach (string item in faVs)
        {
            if (favSearch == item)
            {
                Console.WriteLine(faVs.IndexOf(item));
                break; // Part 8
            }
            else // Part 7
            {
                Console.WriteLine("That might be awesome but can't say that it is one of my favorites.");
            }
        }
        Console.ReadLine();

        //Part 9
        List<string> transForm = new List<string>() { "Optimus Prime", "Bumblebee", "Grimloc", "Kupp", "Arcee", "Bumblebee" };

        Console.WriteLine("Name a Transformer.");
        string botName = Console.ReadLine();
        int comPare = 0;

        foreach (string item in transForm)
        {
            if (botName == item)
            {               
                Console.WriteLine(comPare);
                //Console.WriteLine(transForm.IndexOf(item + "This is the index of "));
                Console.WriteLine(transForm[comPare]);
            }
            else // Part 10
            {
                Console.WriteLine("Sorry, not in this generation.");
            }
            comPare++;
        }
        Console.ReadLine();

        //Part 11
        List<string> lanGuages = new List<string>() { "HTML", "CSS", "CSS", "Javascript", "Python", "C#", "CSS", "C#" };
        List<string> searchLanguages = new List<string>();

        foreach (string item in lanGuages)
        {
            if (searchLanguages.Contains(item))
            {
                Console.WriteLine(item + " has appeared before in the list.");
            }
            else
            {
                searchLanguages.Add(item);
                Console.WriteLine(item);
            }
            
        }
        Console.ReadLine();
    }
}
