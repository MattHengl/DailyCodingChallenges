import io

import pytest
import EmailCampaignManager
from EmailList import EmailList
from Email import Email
import datetime

class Tests:
    @pytest.fixture
    def setup_teardown_fixture(self):
        # Setup code (if needed)
        EmailCampaignManager.email_list = []
        self.test_email_list = EmailList()
        yield
        # Teardown code (if needed)
        EmailCampaignManager.email_list = []

    test_email_campaign = [
        (Email( "mhengl@gmail.com", "Welcome!", "Hello Matt, welcome to our service!", "google.com", datetime.datetime.now().strftime("%m/%d/%Y"), "Company-Oz Corp."), True)
    ]
    @pytest.mark.parametrize("email, expected", test_email_campaign)
    def test_create_email_campaign_with_email(self, setup_teardown_fixture, email, expected):
        assert self.test_email_list.create_email_campaign(email) is True

    def test_create_email_campaign_none_email(self, setup_teardown_fixture, monkeypatch):
        inputs = ["lhengl@gmail.com", "TEST1", "Hello Lori, Welcome to our service", "google.com", datetime.datetime.now().strftime("%m/%d/%Y"), "Company", "Hogwarts"]
        input_iterator = iter(inputs)
        monkeypatch.setattr("builtins.input", lambda _: next(input_iterator))
        assert self.test_email_list.create_email_campaign() is True

    @pytest.mark.parametrize("email, expected", test_email_campaign)
    def test_find_email_campaign_with_id(self, setup_teardown_fixture, email, expected):
        self.test_email_list.create_email_campaign(email)
        assert self.test_email_list.find_email_campaign(email.ID) is email

    @pytest.mark.parametrize("email, expected", test_email_campaign)
    def test_find_email_campaign_with_none_id(self, setup_teardown_fixture, monkeypatch, email, expected):
        self.test_email_list.create_email_campaign(email)
        inputs = ["y", email.ID]
        input_iterator = iter(inputs)
        monkeypatch.setattr("builtins.input", lambda _: next(input_iterator))
        assert self.test_email_list.find_email_campaign() is email

    @pytest.mark.parametrize("email, expected", test_email_campaign)
    def test_delete_email_campaign_with_id(self, setup_teardown_fixture, email, expected):
        self.test_email_list.create_email_campaign(email)
        assert self.test_email_list.delete_email_campaign(email.ID) is True

    @pytest.mark.parametrize("email, expected", test_email_campaign)
    def test_delete_email_campaign_with_none_id(self, setup_teardown_fixture, monkeypatch, email, expected):
        self.test_email_list.create_email_campaign(email)
        inputs = ["y", email.ID]
        input_iterator = iter(inputs)
        monkeypatch.setattr("builtins.input", lambda _: next(input_iterator))
        assert self.test_email_list.delete_email_campaign() is True

