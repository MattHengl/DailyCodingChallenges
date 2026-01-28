import pytest
from Product import Product
from Reporting import Reporting
from Store import Store

class TestProduct:
    @pytest.fixture()
    def setup_teardown(self):
        self.test_inventory = [
            Product("Tomato", 150, None, 20),
            Product("Lettuce", 100, None, 20),
            Product("Watermelon", 300, None, 50)
        ]
        self.test_sending_store = Store("Test Store")
        self.test_sending_store.store_inventory = self.test_inventory
        yield self
        pass
    def test_set_name_success(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "Banana")
        assert Product.set_name() is "Banana"

    def test_set_name_failure(self, monkeypatch):
        inputs = iter(["", "  ", "Orange"])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        assert Product.set_name() is "Orange"

    def test_set_cost_success(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "2.50")
        assert Product.set_cost() == 250

    def test_set_cost_failure(self, monkeypatch):
        inputs = iter(["", "  ", "3.75"])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        assert Product.set_cost() == 375

    def test_set_quantity_success(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "15")
        assert Product.set_quantity() == 15

    def test_set_quantity_failure(self, monkeypatch):
        inputs = iter(["", "  ", "20"])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        assert Product.set_quantity() == 20

    def test_remove_product_success(self, setup_teardown):
        Reporting.current_stock(self.test_sending_store.store_inventory)
        assert Product.remove_product(self.test_sending_store, next((product.sku for product in self.test_sending_store.store_inventory if product.name == "Watermelon"), None)) is True

    def test_remove_product_not_found(self, setup_teardown):
        Reporting.current_stock(self.test_sending_store.store_inventory)
        assert Product.remove_product(self.test_sending_store, "SKU00000") is False