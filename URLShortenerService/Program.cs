using System.Reflection.Metadata.Ecma335;
using System.Xml;
using static ClassLibrary.ClassLibrary;

namespace URLShortenerService;

public class URLShortener
{
    public static List<Url> UrlLibrary = new List<Url>();
    static void Main(string[] args)
    {
        /*
            * Generate short codes for long URLS
            * - Create unique short codes
            * - Ensure no collisions with existing codes
            * - Options for custom aliases
            * Store URL mapping(JSON)
            * "Redirect" functionality - lookup original URL from short code
            * track Analytics for each shortened URL
            * - Number of times accessed
            * - First/Last access timestamps
            * - Access History Log
            * Support URL management
            * - List all shortened URLS
            * - Delete/expire old URLS
            * - Update Destination URLS
            * - Set Expiration dates for temp links
            * Validate URLS before shortening
            * Handle Edge cases(duplicate URLS, invalid characters, etc)
            */
        UrlLibrary = LoadJson<Url>("../../../UrlLibrary.json");
        CheckExpirationDate();
        Menu();
    }
    public static int Add(int x, int y) => x + y;
    public static void Menu()
    {
        bool flag = true;
        do
        {
            Console.WriteLine("What would you like to do today?(List, New, Update, Remove, Open, Exit)");
            var input = Console.ReadLine();
            if (input == null)
            {
                continue;
            }
            switch (input.ToLower().Trim())
            {
                case "list":
                    ListAllUrls();
                    break;
                case "new":
                    NewUrl();
                    break;
                case "update":
                    UpdateUrl(AskingUrl());
                    break;
                case "remove":
                    RemoveUrl(AskingUrl());
                    break;
                case "open":
                    OpenShortUrl(AskingUrl());
                    break;
                case "exit":
                    SaveToJson<Url>(UrlLibrary, "../../../UrlLibrary.json");
                    flag = false;
                    break;
                default:
                    break;
            }
        } while (flag);
    }
    public static Url AskingUrl()
    {
        Console.WriteLine("What shortUrl are you looking for?");
        string? findingShortUrl = Console.ReadLine();
        return UrlLookup(findingShortUrl);
    }
    public static bool UrlExists(string url, string urlType)
    {
        return UrlLibrary.Any(item =>
        urlType == "LongUrl" ? item.LongUrl == url :
        urlType == "ShortUrl" ? item.ShortUrl == url :
        false);
    }
    public static Url UrlLookup(string shortUrl)
    {
        Url foundUrl = null;
        foreach (var item in UrlLibrary)
        {
            if (item.ShortUrl == shortUrl)
            {
                foundUrl = item; break;
            }
        }
        if (foundUrl == null)
        {
            Console.WriteLine("Was not able to find the Url that you are looking for.");
        }
        return foundUrl;
    }
    public static void ListAllUrls()
    {
        if (UrlLibrary.Count != 0) { 
            foreach(var item in UrlLibrary)
            {
                Console.WriteLine(item.ToString());
            }
        }
        else
        {
            Console.WriteLine("There are no Urls to display!");
        }
    }
    public static void NewUrl()
    {
        bool flag = true;
        DateTime parsedExpirationDate = DateTime.MinValue;
        Console.WriteLine("Please enter the full Url.");
        string longUrl = Console.ReadLine();
        string shortUrl = LongUrltoShortUrl();
        Console.WriteLine("Is there an expiration date that you want to add on this url?(Y,N)");
        if (Console.ReadLine().ToLower().Contains("y"))
        {
            do
            {
                Console.WriteLine("Please enter in the expiration date that you would like.(yyyy/MM/dd)");
                string expirationDate = Console.ReadLine();
                if (DateTime.TryParseExact(expirationDate, "yyyy/MM/dd", null, System.Globalization.DateTimeStyles.None, out parsedExpirationDate))
                {
                    Console.WriteLine($"Parsed date: {parsedExpirationDate}");
                    flag = false;
                }
                else
                {
                    Console.WriteLine("That is not a valid DateTime format.");
                }
            } while (flag);
        }
        AddUrlToLibrary(longUrl, shortUrl, flag ? null : (DateTime?)parsedExpirationDate);
    }
    public static void UpdateUrl(Url? url)
    {
        if (url != null)
        {
            Console.WriteLine("What do you want to update?(ShortUrl, LongUrl, ExpirationDate)");
            switch (Console.ReadLine().ToLower().Trim())
            {
                case "shorturl":
                    Console.WriteLine("What do you want the new ShortUrl to be?");
                    url.ShortUrl = Console.ReadLine();
                    break;
                case "longurl":
                    Console.WriteLine("What do you want the new LongUrl to be?");
                    url.LongUrl = Console.ReadLine();
                    break;
                case "expirationdate":
                    Console.WriteLine("What do you want the new ExpirationDate to be?");
                    string desiredExpirationDate = Console.ReadLine();
                    DateTime newExpirationDate;
                    if (DateTime.TryParseExact(desiredExpirationDate, "yyyy/MM/dd", null, System.Globalization.DateTimeStyles.None, out newExpirationDate))
                    {
                        url.ExpirationDate = newExpirationDate;
                    }
                    else
                    {
                        Console.WriteLine("That is not a valid DateTime format.");
                    }
                    break;
                default:
                    break;
            }
        }
    }
    public static void RemoveUrl(Url removalUrl)
    {
        if (removalUrl != null)
        {
            UrlLibrary.Remove(removalUrl);
        }
    }
    public static string LongUrltoShortUrl()
    {
        const string chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        var rnd = new Random();
        string shortUrl;
        do
        {
            shortUrl = "shortu/" + new string(Enumerable.Repeat(chars, 6)
                .Select(s => s[rnd.Next(s.Length)]).ToArray());
        } while (UrlLibrary.Any(u => u.ShortUrl == shortUrl));
        return shortUrl;
    }
    public static void AddUrlToLibrary(string longUrl, string shortUrl, DateTime? expirationDate)
    {
        //Check the library first to see if there is already a long/short form url already?
        if (!UrlExists(longUrl, "LongUrl") && !UrlExists(shortUrl, "ShortUrl"))
        {
            Url newUrl = new Url(longUrl, shortUrl, DateTime.Now, null, expirationDate, 0);
            UrlLibrary.Add(newUrl);
        }
        else
        {
            Console.WriteLine("Url exists in the library already!");
        }
    }
    public static void CheckExpirationDate()
    {
        foreach (var item in UrlLibrary)
        {
            if (item.ExpirationDate == DateTime.Now)
            {
                RemoveUrl(item);
            }
        }
    }
    public static void OpenShortUrl(Url url)
    {
        if (url.ShortUrl != null)
        {
            string chromePath = @"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe";
            if (System.IO.File.Exists(chromePath))
            {
                System.Diagnostics.Process.Start(chromePath, url.LongUrl);
            }

            url.AccessAmount++;
            url.LastAccess = DateTime.Now;
        }
    }
}


public class Url
{
    public string? LongUrl {  get; set; }
    public string? ShortUrl { get; set; }
    public DateTime? FirstAccess {  get; set; }
    public DateTime? LastAccess { get; set; }
    public DateTime? ExpirationDate { get; set; }
    public int AccessAmount { get; set; }
    public Url()
    {
        LongUrl = null;
        ShortUrl = null;
        FirstAccess = null;
        LastAccess = null;
        ExpirationDate = null;
        AccessAmount = 0;
    }
    public Url(string longUrl, string shortUrl, DateTime? firstAccess, DateTime? lastAccess, DateTime? experationDate, int accessAmount)
    {
        LongUrl = longUrl;
        ShortUrl = shortUrl;
        FirstAccess = firstAccess;
        LastAccess = lastAccess;
        ExpirationDate = experationDate;
        AccessAmount = accessAmount;
    }
    public override string ToString()
    {
        return $"\nLongUrl: {LongUrl}\nShortUrl: {ShortUrl}\nFirstAccess: {FirstAccess}\nLastAccess: {LastAccess}\nExpirationDate: {ExpirationDate}\nAccessAmount: {AccessAmount}\n";
    }
}