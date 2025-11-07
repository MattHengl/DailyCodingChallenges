import pytest
import JSONHandler

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