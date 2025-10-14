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
        string expirationDate = null;
        bool flag = true;
        do
        {
            Console.WriteLine("Please enter the full Url.");
            string longUrl = Console.ReadLine();
            if (!string.IsNullOrEmpty(longUrl))
            {
                string shortUrl = LongUrltoShortUrl();
                Console.WriteLine("Is there an expiration date that you want to add on this url?(Y,N)");
                if (Console.ReadLine().ToLower().Contains("y"))
                {
                    Console.WriteLine("Please enter in the expiration date that you would like.(yyyy/MM/dd)");
                    expirationDate = Console.ReadLine();
                    Console.WriteLine($"Expiration date: {expirationDate}");
                }
                AddUrlToLibrary(longUrl, shortUrl, expirationDate);
                flag = false;
            }
            else
            {
                Console.WriteLine("That is not a valid long url.");
            }
        } while (flag);
    }
    public static void UpdateUrl(Url? url)
    {
        bool flag = true;
        if (url != null)
        {
            do
            {
                Console.WriteLine("What do you want to update?(ShortUrl, LongUrl, ExpirationDate)");
                switch (Console.ReadLine().ToLower().Trim())
                {
                    case "shorturl":
                        Console.WriteLine("What do you want the new ShortUrl to be?");
                        url.ShortUrl = Console.ReadLine();
                        flag = true; break;
                    case "longurl":
                        Console.WriteLine("What do you want the new LongUrl to be?");
                        url.LongUrl = Console.ReadLine();
                        flag = true; break;
                    case "expirationdate":
                        Console.WriteLine("What do you want the new ExpirationDate to be?");
                        string desiredExpirationDate = Console.ReadLine();
                        url.ExpirationDate = desiredExpirationDate;
                        flag = true; break;
                    default:
                        Console.WriteLine("Not a valid option, please select a valid option.");
                        break;
                }
            } while (flag);
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
    public static void AddUrlToLibrary(string longUrl, string shortUrl, string expirationDate)
    {
        //Check the library first to see if there is already a long/short form url already?
        if (!UrlExists(longUrl, "LongUrl") && !UrlExists(shortUrl, "ShortUrl"))
        {
            Url newUrl = new Url(longUrl, shortUrl, $"{DateTime.Now.Year}-{DateTime.Now.Month}-{DateTime.Now.Day}", null, expirationDate, 0);
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
            if (item.ExpirationDate == $"{DateTime.Now.Year}-{DateTime.Now.Month}-{DateTime.Now.Day}")
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
            url.LastAccess = $"{DateTime.Now.Year}-{DateTime.Now.Month}-{DateTime.Now.Day}";
        }
    }
}


public class Url
{
    public string? LongUrl {  get; set; }
    public string? ShortUrl { get; set; }
    public string? FirstAccess {  get; set; }
    public string? LastAccess { get; set; }
    public string? ExpirationDate { get; set; }
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
    public Url(string longUrl, string shortUrl, string? firstAccess, string? lastAccess, string? experationDate, int accessAmount)
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