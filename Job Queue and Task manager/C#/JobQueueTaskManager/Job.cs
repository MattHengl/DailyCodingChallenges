using System.ComponentModel.DataAnnotations;

namespace Job;

public class Job
{
    public string? JobName
    {
        get { return JobName; }
        private set
        {
            if (value == null || value == "")
            {
                Console.WriteLine("Do something here to make sure that they can't save a blank name.");
                JobName = "Sleep Job";
            }
            else
            {
                JobName = value;
            }
        }
    }
    public string? JobType 
    { 
        get { return JobType; } 
        private set 
        { 
            if(value == null || value == "")
            {
                Console.WriteLine("Do something here to make sure that they can't save a blank type.");
                JobType = "Sleep";
            }
            else
            {
                JobType = value;
            }
        }
    }
    public DateTime? JobRunDate 
    {
        get { return JobRunDate; }
        private set
        {
            if (value == null)
            {
                Console.WriteLine("Do something here to make sure that they can't save a blank date.");
                JobRunDate = new DateTime(2025, 12, 6);
            }
            else
            {
                JobRunDate = value;
            }
        }
    }
    public string? JobStatus 
    { 
        get; 
        private set; 
    }

    public Job(string name, string type, DateTime jobRunDate)
    {
        JobName = name;
        JobType = type;
        JobRunDate = jobRunDate;
        JobStatus = "Pending";
    }

    public override string ToString()
    {
        return $"JobName: {JobName}\n" +
            $"JobType: {JobType}" +
            $"JobRunDate: {JobRunDate}" +
            $"JobStatus: {JobStatus}";
    }
}
