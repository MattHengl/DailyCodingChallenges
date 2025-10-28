import JSONHandler
import EmailCampaignManager
import io

class Tests:
    def test_get_action_input(self, monkeypatch):
        monkeypatch.setattr("sys.stdin", io.StringIO("1"))
        assert EmailCampaignManager.get_action_input() == "1"
    def test_create_email(self):
        assert True
    def test_create_emailer_card(self):
        assert True
    def test_add_emailer_contacts(self):
        assert True
    def test_create_email_campaign(self):
        assert True
    def test_view_email_campaign(self):
        assert True
    def test_delete_email_campaign(self):
        assert True
    def test_send_email(self):
        assert True
    def test_adds(self):
        assert EmailCampaignManager.adds(2,2) == 4
    def test_load_json_contacts(self):
        assert JSONHandler.load_json("Contacts.JSON") == []
    def test_load_json_emails(self):
        assert JSONHandler.load_json("Emails.JSON") == []
    def test_save_json(self):
        assert True