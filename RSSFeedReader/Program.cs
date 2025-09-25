using System.Data.SqlTypes;
using System.Net;
using System.Security.Principal;
using System.Text.Json;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace RSSFeedReader;

class RSSFeedReader
{
    public static List<Article> personalLibrary = new List<Article>();
    static async Task Main(string[] args)
    {
        /*
         * A console app that fetches and processes RSS reeds from multiple sources
         * The program should:
         * Manage a list of RSS feed URLS(news, blogs, etc.)
         * Fetch and parse RSS/XML feeds using Httpclient
         * Extract key information from each feed item
         * - Title, desc, publication date, link
         * - Author/source name
         * Display feeds in various ways
         * - Latest article
         * - articles from specific sources
         * - articles containing specific keywords
         * Save articles to local storage for offline reading
         * Track which articles have been read vs unread
         * Generate daily/weekly summaries of new content
         * Handle network errors and invalid feeds gravefully
         * Sample RSS feeds to use: BBC News, Reddit, Stack Overflow, blogs, etc
         * 
         * RSS, or Really Simple Syndication, is a web feed format that allows users to receive automatic updates from websites, 
         * blogs, news publishers, and podcasts in a single, centralized location. Rather than visiting each site individually, 
         * users can subscribe to an RSS feed and view all the latest content in a feed reader or aggregator. 
         * 
         */
        personalLibrary = LoadJson();
        await PickWebsite();
        SaveToJson(personalLibrary);
    }
    public static async Task PickWebsite()
    {
        Console.WriteLine("What news site do you want to pull the headlines for?");
        Console.WriteLine("Options:" +
            "- King5\n" + 
            "- King5 Sports\n" + 
            "- BBC\n" + 
            "- NPR\n" +
            "- New York Times\n" + 
            "- The Guardian\n" + 
            "- Al Jazeera\n" + 
            "- ABC News");
        switch (Console.ReadLine().ToLower())
        {
            case string option when option.Contains("king5"):
                await CallWebsite("https://www.king5.com/feeds/syndication/rss/news/local");
                break;
            case string option when option.Contains("sport"):
                await CallWebsite("https://www.king5.com/feeds/syndication/rss/sports/mlb/mariners");
                break;
            case string option when option.Contains("bbc"):
                await CallWebsite("http://feeds.bbci.co.uk/news/world/rss.xml");
                break;
            case string option when option.Contains("npr"):
                await CallWebsite("https://www.npr.org/rss/rss.php?id=1001");
                break;
            case string option when option.Contains("new"):
                await CallWebsite("https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml");
                break;
            case string option when option.Contains("guardian"):
                await CallWebsite("https://www.theguardian.com/world/rss");
                break;
            case string option when option.Contains("jazeera"):
                await CallWebsite("https://www.aljazeera.com/xml/rss/all.xml");
                break;
            case string option when option.Contains("abc"):
                await CallWebsite("https://abcnews.go.com/abcnews/topstories");
                break;
            default:
                Console.WriteLine("That news website isn't an option!");
                break;
        }
    }
    public static List<Article> LoadJson()
    {
        string jsonString = File.ReadAllText("../../../PersonalLibrary.json");
        var accounts = JsonSerializer.Deserialize<List<Article>>(jsonString) ?? new List<Article>();
        return accounts;
    }
    public static void SaveToJson(List<Article> articles)
    {
        string jsonString = JsonSerializer.Serialize(articles, new JsonSerializerOptions { WriteIndented = true });
        File.WriteAllText("../../../PersonalLibrary.json", jsonString);
    }
    public static async Task CallWebsite(string url)
    {
        using (HttpClient client = new HttpClient())
        {
            try
            {
                HttpResponseMessage response = await client.GetAsync(url);
                response.EnsureSuccessStatusCode();
                string responseBody = await response.Content.ReadAsStringAsync();
                //TO SEE THE RAW XML RETURN, UNCOMMENT THIS - Console.WriteLine(responseBody);
                ParseXML(responseBody);
            }
            catch (Exception e)
            {
                Console.WriteLine($"An unexpected error occurred: {e.Message}");
            }
        }
    }
    public static void ParseXML(string xmlString)
    {
        XDocument docFromString = XDocument.Parse(xmlString);

        var items = docFromString.Descendants("item");
        List<Article> articles = new List<Article>();
        Console.WriteLine("\n------------------------------------------------\n");
        foreach (var item in items)
        {
            Article article = new Article(item.Element("title")?.Value ?? string.Empty, 
                item.Element("link")?.Value ?? string.Empty, 
                item.Element("pubDate")?.Value ?? string.Empty, 
                (Regex.Replace(item.Element("description")?.Value ?? string.Empty, "<.*?>", string.Empty)), 
                item.Element("guid")?.Value ?? string.Empty);
            Console.WriteLine(article.ToString());
            articles.Add(article);
        }
        SaveArticle(articles);
    }
    public static void SaveArticle(List<Article> articles)
    {
        Console.WriteLine("Is there an article that you would like to save to your personal library?");
        if (Console.ReadLine()?.ToLower().Contains("y") == true)
        {
            Console.WriteLine("What is the guid of the article you want to save?");
            string? guidToSave = Console.ReadLine();
            if (!string.IsNullOrEmpty(guidToSave))
            {
                foreach (var item in articles)
                {
                    if (item.Guid == guidToSave)
                    {
                        personalLibrary.Add(item);
                    }
                }
            }
        }
    }
}

public class Article
{
    public string Title {  get; set; }
    public string Link { get; set; }
    public string Published { get; set; }
    public string Description { get; set; }
    public string Guid { get; set; }
    public Article(string title, string link, string published, string description, string guid)
    {
        Title = title;
        Link = link;
        Published = published;
        Description = description;
        Guid = guid;
    }
    public Article() 
    {
        Title = "";
        Link = "";
        Published = "";
        Description = "";
        Guid = "";
    }
    public override string ToString()
    {
        return $"Title: {Title}\n" +
                $"Published: {Published}\n" +
                $"Value: {Description}\n" +
                $"Link: {Link}\n" + 
                $"Guid: {Guid}\n";
    }
}