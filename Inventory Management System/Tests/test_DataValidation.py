import pytest
from DataValidation import DataValidation
from Product import Product
from Store import Store


class TestDataValidation:
    @pytest.fixture()
    def setup_teardown(self):
        self.test_inventory = [Product("Tomato", 1.50,"SKU12345",0), Product("Lettuce", 1.00, "SKU12346", 5)]
        self.test_store_list = [Store("Main Warehouse"), Store("Downtown Store"), Store("Matts Store", 12345)]
        self.test_store_list[2].store_inventory = self.test_inventory
        yield self
        pass

    # checking stock
    # Will be giving a product and quantity, if the stock is less than quantity, it should return false
    @pytest.mark.parametrize("product", [Product("Tomato", 1.50, None, 50)])
    def test_check_stock_success(self, product):
        assert DataValidation.check_stock(product, 10) is True

    def test_check_stock_failure(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "0")
        assert DataValidation.check_stock(None, 0) is False

    def test_check_sku_duplicates_success(self, setup_teardown):
        searching_sku = "SKU12347"
        assert DataValidation.check_sku_duplicates(searching_sku, self.test_store_list) is searching_sku

    def test_check_sku_duplicates_found_duplicate(self, setup_teardown):
        DataValidation.check_sku_duplicates("SKU12345", self.test_store_list)

    def test_check_sku_duplicates_failure(self):
        assert DataValidation.check_sku_duplicates("1", "Not a List") is False

    def test_check_store_number_duplicates_success(self, setup_teardown):
        searching_store_number = 12346
        assert DataValidation.check_store_number_duplicates(searching_store_number, self.test_store_list) is searching_store_number

    def test_check_store_number_duplicates_found_duplicate(self, setup_teardown):
        DataValidation.check_store_number_duplicates(12345, self.test_store_list)

    def test_check_store_number_duplicates_failure(self):
        assert DataValidation.check_store_number_duplicates("1", "Not a list") is False

    def test_get_store_success(self, setup_teardown):
        assert DataValidation.get_store(12345, self.test_store_list) == self.test_store_list[2]

    def test_get_store_failure(self, setup_teardown):
        assert DataValidation.get_store(12346, self.test_store_list) is False
