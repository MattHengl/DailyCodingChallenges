using System.Security.Cryptography.X509Certificates;
using URLShortenerService;
using Xunit;
using static UtilityLibrary.UtilityClass;

namespace URLShortenerTest
{
    public class UnitTest1 : IAsyncLifetime
    {
        public async Task InitializeAsync()
        {
            URLShortener.UrlLibrary = LoadJson<Url>("../../../UrlLibrary.json");
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

        [Fact]
        public void UrlExistsGood()
        {
            Assert.True(URLShortener.UrlExists("google.com", "LongUrl"));
        }

        [Fact]
        public void UrlExistsBad()
        {
            Assert.False(URLShortener.UrlExists("facebook.com", "LongUrl"));
        }

        [Fact]
        public void UrlLookupGood()
        {
           Assert.Equivalent(new Url("bing.com", "shortu/fJyt3g", new DateTime(2025, 10, 06, 15, 36, 23, 834, DateTimeKind.Local), null, null, 0), URLShortener.UrlLookup("shortu/fJyt3g"));
        }

        [Fact]
        public void UrlLookupBad()
        {
            Assert.NotEqual(new Url("chrome.com", "shortu/1122g", new DateTime(2025, 10, 06, 15, 36, 23, 834, DateTimeKind.Local), null, null, 0), URLShortener.UrlLookup("shortu/fJyt3g"));
        }
        [Fact]
        public void NewUrlGood()
        {

        }
        [Fact]
        public void NewUrlBad()
        {
            Assert.
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