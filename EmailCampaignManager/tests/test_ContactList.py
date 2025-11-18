from ContactCard import Contact
import pytest
import io
import EmailCampaignManager
from ContactList import ContactList

class Tests:
    @pytest.fixture
    def setup_teardown_fixture(self):
        # Setup code (if needed)
        EmailCampaignManager.contact_list = []
        self.test_contact_list = ContactList()
        yield
        # Teardown code (if needed)
        EmailCampaignManager.contact_list = []

    test_contact_card = [
        (Contact("Matt","Hengl","mhengl@gmail.com","Oz Corp."), True)
    ]
    @pytest.mark.parametrize("contact, expected", test_contact_card)
    def test_add_card_to_contacts_with_contact(self, setup_teardown_fixture, contact, expected):
        assert self.test_contact_list.add_card_to_contacts(contact) is expected

    def test_add_card_to_contacts_with_none_contact(self, setup_teardown_fixture, monkeypatch):
        inputs = ["Lori", "Hengl", "lhengl@gmail.com", "Hogwarts"]
        input_iterator = iter(inputs)
        monkeypatch.setattr("builtins.input", lambda _: next(input_iterator))
        assert self.test_contact_list.add_card_to_contacts() is True

    @pytest.mark.parametrize("contact, expected", test_contact_card)
    def test_remove_contact_card_with_contact(self, setup_teardown_fixture, contact, expected):
        self.test_contact_list.add_card_to_contacts(contact)
        self.test_contact_list.remove_contact_card(contact)
        assert self.test_contact_list.find_contact(contact.email) is False

    @pytest.mark.parametrize("contact, expected", test_contact_card)
    def test_remove_contact_card_with_none_contact(self, setup_teardown_fixture, monkeypatch, contact, expected):
        monkeypatch.setattr("sys.stdin", io.StringIO("mhengl@gmail.com"))
        self.test_contact_list.add_card_to_contacts(contact)
        self.test_contact_list.remove_contact_card()
        assert self.test_contact_list.find_contact(contact.email) is False

    def test_remove_contact_card_empty_list(self, setup_teardown_fixture):
        assert self.test_contact_list.remove_contact_card() is False

    @pytest.mark.parametrize("contact, expected", test_contact_card)
    def test_find_contact(self, setup_teardown_fixture, contact, expected):
        self.test_contact_list.add_card_to_contacts(contact)
        assert self.test_contact_list.find_contact(contact.email) is contact

    @pytest.mark.parametrize("contact, expected", test_contact_card)
    def test_find_contact_fail(self, setup_teardown_fixture, contact, expected):
        self.test_contact_list.add_card_to_contacts(contact)
        assert self.test_contact_list.find_contact("lhengl@gmail.com") is False
