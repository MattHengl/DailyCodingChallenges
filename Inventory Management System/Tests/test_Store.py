import pytest
from Product import Product
from Store import Store

class TestStore:
    @pytest.fixture()
    def setup_teardown(self):
        self.test_inventory = [
            Product("Tomato", 1.50, None,20),
            Product("Lettuce", 1.00, None,20),
            Product("Watermelon", 3.00, None,50)
        ]
        self.test_sending_store = Store("Sending Store")
        self.test_sending_store.store_inventory = self.test_inventory
        self.test_receiving_store = Store("Receiving Store")
        yield self
        pass

    def test_store_name_success(self, monkeypatch):
        inputs = iter(["My Test Store"])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        store = Store()
        assert store.store_name == "My Test Store"

    def test_store_name_failure(self, monkeypatch):
        inputs = iter(["", "  ", "Another Store"])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        store = Store()
        assert store.store_name == "Another Store"

    #sending_store, receiving_store, sku, quantity
    def test_send_items_success(self, setup_teardown):
        assert Store.send_items(self.test_sending_store,
                                self.test_receiving_store,
                                next(p.sku for p in self.test_sending_store.store_inventory if p.name == "Watermelon"),
                                20) is True

    def test_send_items_insufficient_quantity(self, setup_teardown):
        assert Store.send_items(self.test_sending_store,
                                self.test_receiving_store,
                                next(p.sku for p in self.test_sending_store.store_inventory if p.name == "Lettuce"),
                                30) is False

    def test_send_items_sku_not_found(self, setup_teardown):
        assert Store.send_items(self.test_sending_store,
                                self.test_receiving_store,
                                "SKU00000",
                                10) is False

    def test_send_item_new_product_added(self, setup_teardown):
        sku = next(p.sku for p in self.test_sending_store.store_inventory if p.name == "Tomato")
        Store.send_items(self.test_sending_store,
                                self.test_receiving_store,
                                sku,
                                10)
        receiving_product = next((p for p in self.test_receiving_store.store_inventory if p.sku == sku), None)
        assert receiving_product.quantity == 10

    def test_look_for_store_success(self, monkeypatch):
        inputs = iter(["My Test Store"])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        test_stores = [Store("My Test Store")]
        assert Store.look_for_store("My Test Store", test_stores) is True

    def test_look_for_store_failure(self, monkeypatch):
        inputs = iter(["Nonexistent Store"])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        test_stores = [Store("My Test Store")]
        assert Store.look_for_store("Nonexistent Store", test_stores) is False