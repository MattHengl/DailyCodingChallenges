using URLShortenerService;
using System.Collections;
using Xunit;
using static ClassLibrary.ClassLibrary;

namespace URLShortenerTest
{
    public class DataGenerator : IEnumerable<object[]>
    {
        private readonly List<object[]> _data = new List<object[]>
        {
            new object[] { "chrome.com", "shortu/1122g", $"2025-10-{DateTime.Now.Day}", null, null, 0 }
        };
        public IEnumerator<object[]> GetEnumerator() => _data.GetEnumerator();

        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
    }
    public class UnitTest1 : IAsyncLifetime
    {
        public Task InitializeAsync()
        {
            URLShortener.UrlLibrary = LoadJson<Url>("../../../UrlLibrary.json");
            return Task.CompletedTask;
        }
        
        [Fact]
        public void AddGood()
        {
            Assert.Equal(4, URLShortener.Add(2, 2));
        }
        //[Fact]
        //public void AddBad()
        //{
        //    Assert.Equal(5, URLShortener.Add(2, 2));
        //}

        //[Theory]
        //[InlineData(4,2,2)]
        //[InlineData(5,3,2)]
        //public void TheoryTesting(int expected, int value1, int value2)
        //{
        //    Assert.Equal(expected, URLShortener.Add(value1, value2));
        //}

        [Theory]
        [InlineData("google.com", "LongUrl")]
        [InlineData("shortu/z7D97d", "ShortUrl")]
        public void UrlExists(string longUrl, string urlType)
        {
            Assert.True(URLShortener.UrlExists(longUrl, urlType));
        }

        [Theory]
        [InlineData("facebook.com", "LongUrl")]
        [InlineData("shortu/112233", "ShortUrl")]
        public void UrlExistsBad(string shortUrl, string uylType)
        {
            Assert.False(URLShortener.UrlExists(shortUrl, uylType));
        }

        [Theory]
        [InlineData("bing.com", "shortu/fJyt3g", "2025-10-06", null, null, 0)]
        public void UrlLookupGood(string longUrl, string shortUrl, string firstAccess, string? lastAccess, string? expirationDate, int accessAmount)
        {
            Assert.Equivalent(new Url(longUrl, shortUrl, firstAccess, lastAccess, expirationDate, accessAmount), URLShortener.UrlLookup(shortUrl));
        }

        [Theory]
        [ClassData(typeof(DataGenerator))]
        public void UrlLookupBad(string longUrl, string shortUrl, string firstAccess, string? lastAccess, string? expirationDate, int accessAmount)
        {
            Assert.NotEqual(new Url(longUrl, shortUrl, firstAccess, lastAccess, expirationDate, accessAmount), URLShortener.UrlLookup("shortu/fJyt3g"));
        }
        [Theory]
        //[InlineData("chrome.com", "shortu/1122g", "2025-10-14", null, null, 0)]
        [ClassData(typeof(DataGenerator))]
        public void AddUrlToLibraryGood(string longUrl, string shortUrl, string firstAccess, string? lastAccess, string? expirationDate, int accessAmount)
        {
            Assert.Multiple(
                () => Assert.True(URLShortener.AddUrlToLibrary(longUrl, shortUrl, expirationDate)),
                () => Assert.Equivalent(new Url(longUrl, shortUrl, firstAccess, lastAccess, expirationDate, accessAmount), URLShortener.UrlLookup(shortUrl))
            );
            //Assert.Contains(new Url(longUrl, shortUrl, firstAccess, lastAccess, expirationDate, accessAmount), URLShortener.UrlLibrary); //<--- Check on why this didn't work?
            //Assert.Equivalent(new Url(longUrl, shortUrl, firstAccess, lastAccess, expirationDate, accessAmount), URLShortener.UrlLookup(shortUrl));
        }

        //Testing to see if the url that is wanting to be added to the Library already exists in the library or not
        [Theory]
        [InlineData("google.com", "shortu/z7D97d", "2025-09-30", "2025-09-30", null, 2)]
        public void AddUrlToLibraryBad(string longUrl, string shortUrl, string firstAccess, string? lastAccess, string? expirationDate, int accessAmount)
        {
            Assert.Multiple(
                () => Assert.False(URLShortener.AddUrlToLibrary(longUrl, shortUrl, expirationDate)),
                () => Assert.Equivalent(new Url(longUrl, shortUrl, firstAccess, lastAccess, expirationDate, accessAmount), URLShortener.UrlLookup(shortUrl))
            );
        }

        //Takes a URL in to remove the Url from the UrlLibrary
        [Theory]
        [ClassData(typeof(DataGenerator))]
        public void RemoveUrlGood(string longUrl, string shortUrl, string firstAccess, string? lastAccess, string? expirationDate, int accessAmount)
        {
            URLShortener.AddUrlToLibrary(longUrl, shortUrl, expirationDate);
            URLShortener.RemoveUrl(URLShortener.UrlLookup(shortUrl));
            Assert.DoesNotContain(new Url(longUrl, shortUrl, firstAccess, lastAccess, expirationDate, accessAmount), URLShortener.UrlLibrary);
        }

        [Theory]
        [InlineData("chrome.com", "shortu/1122g", "2025-10-14", null, "2025-10-14", 0)]
        public void CheckExpirationDateGood(string longUrl, string shortUrl, string firstAccess, string? lastAccess, string? expirationDate, int accessAmount)
        {
            URLShortener.AddUrlToLibrary(longUrl, shortUrl, expirationDate);
            URLShortener.CheckExpirationDate();
            Assert.DoesNotContain(new Url(longUrl, shortUrl, firstAccess, lastAccess, expirationDate, accessAmount), URLShortener.UrlLibrary);
        }
        public async Task DisposeAsync()
        {
            
        }
    }
}