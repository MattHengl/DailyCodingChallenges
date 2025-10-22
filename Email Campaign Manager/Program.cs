class EmailManager
{
    static void Main(string[] args)
    {
        /*
         * Manage Contact List
         * - Add/Remove/Import contacts
         * - Organize contacts into groups/segments
         * - store contact info(name, email, custom fields)
         * - Handle Duplicate detection and merge
         * 
         * Create Email Campaigns
         * - design email templates with placeholders
         * - preview emails with actual contact data subbed
         * - schedule campaigns for future sending
         * - A/D test support
         * 
         * Send Emails
         * - use SMTP to actuall send emails( or sim if you prefer)
         * - Batch processing with rate limiting (Dont send all at once)
         * - Personalize each email with contact-specific data
         * - Handle send failures and rety logic
         * 
         * Track Campaign Performance
         * - Delivery status (sent/failed/pending)
         * - Open Tracking (using tracking pixels - sim this)
         * - Click tracking for links in emails
         * - Unsubscribe management
         * - generate campaign reports and stats
         * 
         * Data Persistence with JSON or SQLlite
         * 
         * Safety note: If actually sending emails, use a test SMTP service like Mailtrap or Ethereal to avoid spamming real addresses.
         * 
         */
    }
}
class EmailInfo
{
    public string FirstName { get; set; }
    public string LastName { get; set; }
    public string Email { get; set; }
    public EmailInfo(string firstName, string lastName, string email)
    {
        FirstName = firstName;
        LastName = lastName;
        Email = email;
    }
}

class Email
{
    public string Sender {  get; set; }
    public string Reciever { get; set; }
    public string Content { get; set; }
    public string Url { get; set; }
    public int UrlClicks { get; set; }
    public Email(string sender, string reciever, string content, string url, int urlClicks)
    {
        Sender = sender;
        Reciever = reciever;
        Content = content;
        Url = url;
        UrlClicks = urlClicks;
    }
}
