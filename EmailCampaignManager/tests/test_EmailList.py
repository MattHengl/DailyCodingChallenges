import pytest

import ContactCard
import ContactList
import EmailCampaignManager
import JSONHandler
import EmailList
import Email
import datetime

class Tests:
    @pytest.fixture
    def clear_json_fixture(self):
        filenames = ["Emails.JSON"]
        # Setup code (if needed)
        EmailCampaignManager.email_list = []
        for filename in filenames:
            JSONHandler.clear_json_file(filename)
        yield
        # Teardown code (if needed)
        EmailCampaignManager.email_list = []
        for filename in filenames:
            JSONHandler.clear_json_file(filename)

    test_email_campaign = [
        (Email.Email(777, "mhengl@gmail.com", "Welcome!", "Hello Matt, welcome to our service!", "google.com", datetime.datetime.now(), "Company-Oz Corp."), True)
    ]
    @pytest.mark.parametrize("email, expected", test_email_campaign)
    def test_create_email_campaign(self, clear_json_fixture, email, expected):
        assert EmailList.create_email_campaign(EmailCampaignManager.email_list, email) is True

    def test_create_email_campaign_fail(self, clear_json_fixture, email = 1):
        assert EmailList.create_email_campaign("FAKELIST", email) is False

    empty_email_campaign = [(None, False)]
    @pytest.mark.parametrize("email, expected", empty_email_campaign)
    def test_create_email_campaign_empty(self, clear_json_fixture, email, expected):
        assert EmailList.create_email_campaign(EmailCampaignManager.email_list, email) is expected

    @pytest.mark.parametrize("email, expected", test_email_campaign)
    def test_view_all_email_campaigns(self, clear_json_fixture, email, expected):
        EmailList.create_email_campaign(EmailCampaignManager.email_list, email)
        assert EmailList.view_all_email_campaigns(EmailCampaignManager.email_list) is True
    def test_view_all_email_campaigns_fail(self):
        assert EmailList.view_all_email_campaigns(EmailCampaignManager.email_list) is False
    def test_view_all_email_campaigns_empty_list(self):
        assert EmailList.view_all_email_campaigns(EmailCampaignManager.email_list) is False

    @pytest.mark.parametrize("email, expected", test_email_campaign)
    def test_find_email_campaign(self, clear_json_fixture, email , expected):
        EmailList.create_email_campaign(EmailCampaignManager.email_list, email)
        assert EmailList.find_email_campaign(EmailCampaignManager.email_list, email.ID) is email
    def test_find_email_campaign_empty_list(self):
        assert EmailList.find_email_campaign(EmailCampaignManager.email_list, 777) == {}
    def test_find_email_campaign_cant_find(self):
        assert EmailList.find_email_campaign(EmailCampaignManager.email_list, 777) == {}

    @pytest.mark.parametrize("email, expected", test_email_campaign)
    def test_check_date_to_send_auto_email(self, clear_json_fixture, email, expected):
        EmailList.create_email_campaign(EmailCampaignManager.email_list, email)
        assert EmailList.check_date_to_send_auto_email(EmailCampaignManager.email_list) > 0
    def test_check_date_to_send_auto_email_empty(self):
        assert EmailList.check_date_to_send_auto_email(EmailCampaignManager.email_list) == 0

    @pytest.mark.parametrize("email, expected", test_email_campaign)
    def test_send_email(self, email, expected):
        ContactList.add_card_to_contacts(EmailCampaignManager.contact_list, ContactCard.Contact("Matt","Hengl","mhengl@gmail.com","Oz Corp."))
        assert EmailList.send_email(email, EmailCampaignManager.contact_list) is True
        JSONHandler.clear_json_file("Contacts.JSON")
    def test_send_email_fail(self, email = None):
        assert EmailList.send_email(email, EmailCampaignManager.contact_list) is False
    @pytest.mark.parametrize("email, expected", test_email_campaign)
    def test_send_email_contact_list_empty(self, email, expected):
        assert EmailList.send_email(email, EmailCampaignManager.contact_list) is False