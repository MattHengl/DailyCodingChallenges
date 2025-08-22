using System.Net;

namespace LogParser;

class LogParser
{
    static void Main(string[] args)
    {
        //Read in the log file
        //Start at the first line and go until there are no more lines to read in
        //Example Line: 192.168.1.1 - - [10/Oct/2023:13:55:36 +0000] "GET /home HTTP/1.1" 200 2326
        //Parse the line into IP address, timestamp, HTTP method, URL path, status code, and response size
        //Once each piece has been gathered, display each piece of data in a pretty way
        //Write all this info to a LogSummary page
        //Make sure to handle malformed logfile lines
        
        StreamReader fileReader = new StreamReader("../../../LogFile.txt"/*Console.ReadLine()*/);
        string? line;
        while ((line = fileReader.ReadLine()) != null)
        {
            try
            {
                List<string> lineContent = new List<string>();

                int ipEnd = line.IndexOf(" - - ");
                string ip = line.Substring(0, ipEnd);
                lineContent.Add($"IP Address: {ip}");

                int tsStart = line.IndexOf('[') + 1;
                int tsEnd = line.IndexOf(']');
                string timestamp = line.Substring(tsStart, tsEnd - tsStart);
                lineContent.Add($"Timestamp: {timestamp}");

                int reqStart = line.IndexOf('"') + 1;
                int reqEnd = line.IndexOf('"', reqStart);
                string request = line.Substring(reqStart, reqEnd - reqStart);

                string[] reqParts = request.Split(' ');
                string method = reqParts[0];
                lineContent.Add($"Method: {method}");
                string url = reqParts[1];
                lineContent.Add($"URL: {url}");
                string httpVersion = reqParts[2];
                lineContent.Add($"HTTP Version: {httpVersion}");

                string afterRequest = line.Substring(reqEnd + 1).Trim();
                string[] statusAndSize = afterRequest.Split(' ', StringSplitOptions.RemoveEmptyEntries);
                string statusCode = statusAndSize[0];
                lineContent.Add($"Status Code: {statusCode}");
                string responseSize = statusAndSize[1];
                lineContent.Add($"Response Size: {responseSize}");

                WriteList( lineContent );
            }
            catch
            {
                Console.WriteLine("Malformed log line: " + line);
            }
        }
    }
    public static void WriteList(List<string> list)
    {
        using (StreamWriter writer = new StreamWriter("../../../PrettyLogFile.txt", append: false))
        {
            foreach (string content in list)
            {
                Console.WriteLine($"{content}");
                writer.WriteLine(content);
            }
        }
    }
}




/*
 * 192.168.1.1 - - [10/Oct/2023:13:55:36 +0000] "GET /home HTTP/1.1" 200 2326
 * 
 * 192.168.1.1
 * [10/Oct/2023:13:55:36 +0000] "GET /home HTTP/1.1" 200 2326
 * 
 * 192.168.1.1
 * 10/Oct/2023:13:55:36 +0000
 * "GET /home HTTP/1.1" 200 2326
 * 
 * 192.168.1.1
 * 10/Oct/2023:13:55:36 +0000
 * GET 
 * home HTTP
 * 1.1 
 * 200 2326
 * 
 * 192.168.1.1
 * 10/Oct/2023:13:55:36 +0000
 * GET 
 * home HTTP
 * 1.1 
 * 200 
 * 2326
 */