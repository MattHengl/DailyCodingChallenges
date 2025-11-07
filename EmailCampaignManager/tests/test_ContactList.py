import ContactCard
import pytest
import io
import EmailCampaignManager
import JSONHandler
import ContactList

class Tests:
    @pytest.fixture
    def clear_json_fixture(self):
        filenames = ["Contacts.JSON"]
        # Setup code (if needed)
        EmailCampaignManager.contact_list = []
        for filename in filenames:
            JSONHandler.clear_json_file(filename)
        yield
        # Teardown code (if needed)
        EmailCampaignManager.contact_list = []
        for filename in filenames:
            JSONHandler.clear_json_file(filename)

    test_contact_card = [
        (ContactCard.Contact("Matt","Hengl","mhengl@gmail.com","Oz Corp."), True)
    ]
    @pytest.mark.parametrize("contact, expected", test_contact_card)
    def test_add_card_to_contacts(self, clear_json_fixture, contact, expected):
        assert ContactList.add_card_to_contacts(EmailCampaignManager.contact_list, contact) is expected

    def test_add_card_to_contacts_fail(self, clear_json_fixture, contact = 1, expected = False):
        assert ContactList.add_card_to_contacts("FAKELIST", contact) is expected

    empty_contact_card = [ContactCard.Contact("","","",""), False]
    @pytest.mark.parametrize("contact, expected", test_contact_card)
    def test_add_card_to_contacts_empty(self, clear_json_fixture, contact, expected):
        assert ContactList.add_card_to_contacts(EmailCampaignManager.contact_list, contact) is expected

    @pytest.mark.parametrize("contact, expected", test_contact_card)
    def test_remove_contact_card(self, clear_json_fixture, monkeypatch, contact, expected):
        monkeypatch.setattr("sys.stdin", io.StringIO("mhengl@gmail.com"))
        ContactList.remove_contact_card(EmailCampaignManager.contact_list, contact)
        assert EmailCampaignManager.contact_list == []

    @pytest.mark.parametrize("contact, expected", test_contact_card)
    def test_find_contact(self, clear_json_fixture, contact, expected):
        ContactList.add_card_to_contacts(EmailCampaignManager.contact_list, contact)
        assert ContactList.find_contact(EmailCampaignManager.contact_list, contact.email) is contact

    @pytest.mark.parametrize("contact, expected", test_contact_card)
    def test_find_contact_fail(self, contact, expected):
        ContactList.add_card_to_contacts(EmailCampaignManager.contact_list, contact)
        assert ContactList.find_contact(EmailCampaignManager.contact_list, "lhengl@gmail.com") is False