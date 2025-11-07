import JSONHandler
import ContactCard
import pytest

class Tests:
    @pytest.fixture
    def clear_json_fixture(self):
        filenames = ["Contacts.JSON", "Emails.JSON"]
        # Setup code (if needed)
        for filename in filenames:
            JSONHandler.clear_json_file(filename)
        yield
        # Teardown code (if needed)
        for filename in filenames:
            JSONHandler.clear_json_file(filename)
    load_json_test_data = [
        ("Contacts.JSON", []),
        ("Emails.JSON", []),
        ("NonExistentFile.JSON", False)
    ]

    @pytest.mark.parametrize("filename, expected", load_json_test_data)
    def test_load_json(self, filename, expected):
        assert JSONHandler.load_json(filename) == expected

    save_json_test_data = [
        ("Contacts.JSON", [
            ContactCard.Contact("Matt", "Hengl", "mhengl@gmail.com", "Oz Corp.").__dict__,
            ContactCard.Contact("Lori", "Hengl", "lhengl@gmail.com", "Oz Corp.").__dict__
        ], True),
        ("Emails.JSON", [], True)
    ]

    @pytest.mark.parametrize("filename, save_list, expected", save_json_test_data)
    def test_save_json(self, clear_json_fixture, filename, save_list, expected):
        assert JSONHandler.save_json(filename, save_list) is expected