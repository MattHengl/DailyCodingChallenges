import EmailCampaignManager
import io

class Tests:
    def test_get_action_input(self, monkeypatch):
        monkeypatch.setattr("sys.stdin", io.StringIO("1"))
        assert EmailCampaignManager.get_action_input() == "1"
