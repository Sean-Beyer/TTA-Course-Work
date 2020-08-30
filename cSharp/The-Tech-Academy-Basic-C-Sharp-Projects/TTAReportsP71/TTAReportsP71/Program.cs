using System;




class Program
{
    static void Main()
    {
    Console.WriteLine("The Tech Academy");
    Console.WriteLine("Student Daily Report");
    Console.ReadLine();
    Console.WriteLine("What is your name?");
    string yourName = Console.ReadLine();
    Console.WriteLine("Your name is: " + yourName);
    Console.ReadLine();
    Console.WriteLine("What course are you on?");
    string yourCourse = Console.ReadLine();
    Console.WriteLine("Your current course: " + yourCourse);
    Console.ReadLine();
    Console.WriteLine("What page are you on?");
    string yourPage = Console.ReadLine();
    Console.WriteLine("Your current page: " + yourPage);
    Console.ReadLine();
    Console.WriteLine("Do you need help with anything?");
    bool noHelp = false;
    bool yesHelp = true;
    Console.WriteLine("Perfect " + noHelp);
    Console.WriteLine("Someone will contact you. " + yesHelp);
    Console.ReadLine();
    Console.WriteLine("Were there any positive experiences you’d like to share? Please give specifics.");
    string posiTives = Console.ReadLine();
    Console.WriteLine(posiTives + "Glad to hear it!");
    Console.ReadLine();
    Console.WriteLine("Is there any other feedback you’d like to provide? Please be specific.");
    string feedBack = Console.ReadLine();
    Console.WriteLine(feedBack + "Excellent!");
    Console.ReadLine();
    Console.WriteLine("How many hours did you study today?");
    string studyTime = Console.ReadLine();
    string hoursStudied = Convert.ToString(studyTime);
    Console.WriteLine("You've studied a total of: " + hoursStudied + "Correct?");
    Console.ReadLine();
    bool corRect = false;
    bool noPe = true;
    Console.WriteLine("Right on!", corRect);
    Console.WriteLine("Ok", noPe);
    Console.ReadLine();
    Console.WriteLine("Thank you for your answers. An Instructor will respond to this shortly.");
    Console.WriteLine("Have a great day!");
    Console.ReadLine();
    }
}

