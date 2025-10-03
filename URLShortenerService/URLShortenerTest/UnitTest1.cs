using URLShortenerService;
using Xunit;

namespace URLShortenerTest
{
    public class UnitTest1
    {
        [Fact]
        public void AddGood()
        {
            Assert.Equal(4, URLShortener.Add(2, 2));
        }
        [Fact]
        public void AddBad()
        {
            Assert.Equal(5, URLShortener.Add(2, 2));
        }
    }
}