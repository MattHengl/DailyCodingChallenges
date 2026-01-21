import pytest
import ManagementMain
import Menu
from Store import Store


class TestMenu:
    @pytest.fixture()
    def setup_teardown(self):
        self.test_sending_store = Store("Test Store")
        ManagementMain.stores_list.append(self.test_sending_store)
        yield self
        pass

    def test_get_and_check_for_store_success(self, setup_teardown, monkeypatch):
        inputs = iter(["Test Store"])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        assert Menu.get_and_check_for_store("Test Store") == self.test_sending_store

    def test_get_and_check_for_store_failure(self, setup_teardown, monkeypatch):
        inputs = iter(["Nonexistent Store"])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        assert Menu.get_and_check_for_store("Nonexistent Store") is None