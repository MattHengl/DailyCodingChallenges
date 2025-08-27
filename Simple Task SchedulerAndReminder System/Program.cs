using System;
using System.IO.Compression;
using System.Security.Cryptography.X509Certificates;
using System.Text.Json;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace TaskScheduler;

public class TaskScheduler
{
    public static List<MyTask> myTasks = new List<MyTask>();
    static void Main(string[] args)
    {
        //Read/Write to a JSON file
        //Read
        //Once the JSON is read in, it will display the closest and the highest priority of tasks in the list
        //Once it reads the tasks in, it will delete any tasks that are past due
        //Write
        //The user can input another task
        //Date
        //Time
        //Priority
        //Category
        //Once the user puts the task in, it'll add to the JSON file at the end
        LoadJson();
        do
        {
            Console.WriteLine("Do you want to see the current tasks or input a new one?");
            string userInput = Console.ReadLine().ToLower();
            if (userInput.Contains("current"))
            {
                Console.WriteLine("Current");
                PrintList();
            }
            else if (userInput.Contains("input"))
            {
                Console.WriteLine("Input");
                GetNewTask();
            }
            else
            {
                Console.WriteLine("That's not a valid option");
            }
                Console.WriteLine("Do you want to continue checking tasks/inputting new tasks?(Y/N)");
        } while (Console.ReadLine().ToLower().Contains("y"));
        SaveToJson();
    }
    public static void PrintList()
    {
        foreach (var task in myTasks)
        {
            if (task.Archive == false)
            {
                Console.WriteLine(task.ToString());
            }
        }
    }
    public static void GetNewTask()
    {
        int hour = 0;
        int minute = 0;
        Console.WriteLine("What is the name of the task you want to add?");
        string taskName = Console.ReadLine();
        Console.WriteLine("What is the date of this task or event?(dd/mm/yyyy)");
        string dateTime = Console.ReadLine();
        Console.WriteLine("What is the priority of this task?(0-9)");
        int priority = int.Parse(Console.ReadLine());
        Console.WriteLine("Is there a specific time that this task is at?(Y/N)");
        if (Console.ReadLine().ToLower().Contains("y"))
        {
            Console.Write("What time is this task going to be at? ");
            string exactTime = Console.ReadLine();
            string[] time = exactTime.Split(":");
            hour = int.Parse(time[0]);
            minute = int.Parse(time[1]);
        }

        string[] dateInts = dateTime.Split("/");
        int day = int.Parse(dateInts[0]);
        int month = int.Parse(dateInts[1]);
        int year = int.Parse(dateInts[2]);

        myTasks.Add(new MyTask(new DateTime(year, month, day, hour, minute, 0), taskName, priority, false));
    }
    public static void LoadJson()
    {
        string jsonString = File.ReadAllText("../../../CurrentTasks.json");
        myTasks = JsonSerializer.Deserialize<List<MyTask>>(jsonString) ?? new List<MyTask>();
    }
    public static void SaveToJson()
    {
        string jsonString = JsonSerializer.Serialize(myTasks, new JsonSerializerOptions { WriteIndented = true });
        File.WriteAllText("../../../CurrentTasks.json", jsonString);
    }

    public class MyTask {
        public DateTime Date { get; set; }
        public string TaskName { get; set; }
        public int Priority { get; set; }
        public bool Archive { get; set; }

        public MyTask(DateTime date, string taskName, int priority, bool archive){
            Date = date;
            TaskName = taskName;
            Priority = priority;
            Archive = archive;
        }
        public string ToString()
        {
            return "Date: " + Date.ToString() + "\nTask Name: " + TaskName + "\nPriority: " + Priority;
        }
    }
}
