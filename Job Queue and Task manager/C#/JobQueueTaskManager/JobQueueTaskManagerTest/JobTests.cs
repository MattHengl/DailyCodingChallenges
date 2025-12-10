using Xunit;

namespace JobQueueTaskManagerTest;

public class JobTests
{
    [Fact]
    public void SucessfulTest()
    {
        Assert.True(true);
    }

    [Fact]
    public void UnsuccessfulTest()
    {
        Assert.False(true);
    }
}
