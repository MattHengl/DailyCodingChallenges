using URLShortenerService;
using System.Collections;
using Xunit;
using static ClassLibrary.ClassLibrary;

namespace URLShortenerTest
{
    public class GoodDataGenerator : IEnumerable<object[]>
    {
        private readonly List<object[]> _data = new List<object[]>
        {
            new object[] { "bing.com", "shortu/fJyt3g", "2025-10-06", null, null, 0 }
        };
        public IEnumerator<object[]> GetEnumerator() => _data.GetEnumerator();

        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
    }
    public class BadDataGenerator : IEnumerable<object[]>
    {
        private readonly List<object[]> _data = new List<object[]>
        {
            new object[] { "chrome.com", "shortu/1122g", "2025-10-06", null, null, 0 }
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
        [InlineData("chrome.com", "shortu/1122g", "2025-10-06", null, null, 0)]
        public void UrlLookupBad(string longUrl, string shortUrl, string firstAccess, string? lastAccess, string? expirationDate, int accessAmount)
        {
            Assert.NotEqual(new Url(longUrl, shortUrl, firstAccess, lastAccess, expirationDate, accessAmount), URLShortener.UrlLookup("shortu/fJyt3g"));
        }
        [Theory]
        [InlineData("chrome.com", "shortu/1122g", "2025-10-13", null, null, 0)]
        public void NewUrlGood(string longUrl, string shortUrl, string firstAccess, string? lastAccess, string? expirationDate, int accessAmount)
        {
            URLShortener.AddUrlToLibrary(longUrl, shortUrl, expirationDate);
            //Assert.Contains(new Url(longUrl, shortUrl, firstAccess, lastAccess, expirationDate, accessAmount), URLShortener.UrlLibrary); <--- Check on why this didn't work?
            Assert.Equivalent(new Url(longUrl, shortUrl, firstAccess, lastAccess, expirationDate, accessAmount), URLShortener.UrlLookup(shortUrl));
        }
        [Fact]
        public void UpdateUrlGood()
        {
            
        }

        [Fact]
        public void UpdateUrlBad()
        {

        }

        [Fact]
        public void RemoveUrlGood()
        {

        }

        [Fact]
        public void RemoveUrlBad()
        {

        }

        [Fact]
        public void LongUrltoShortUrlGood()
        {

        }

        [Fact]
        public void LongUrltoShortUrlBad()
        {

        }

        [Fact]
        public void AddUrlToLibraryGood()
        {

        }

        [Fact]
        public void AddUrlToLibraryBad()
        {

        }

        [Fact]
        public void CheckExpirationDateGood()
        {

        }

        [Fact]
        public void CheckExpirationDateBad()
        {

        }

        [Fact]
        public void OpenShortUrlGood()
        {

        }

        [Fact]
        public void OpenShortUrlBad()
        {

        }
        public async Task DisposeAsync()
        {
            
        }
    }
}