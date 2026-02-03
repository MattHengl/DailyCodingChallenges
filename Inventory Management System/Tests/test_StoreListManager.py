import pytest
from Product import Product
from Store import Store
from StoreListManager import stores_list

class TestStoreListManager:
    @pytest.fixture()
    def setup_teardown(self):
        self.test_inventory = [Product("Tomato", 1.50, "SKU12345", 0), Product("Lettuce", 1.00, "SKU12346", 5)]
        stores_list.extend_stores(
            [Store("Main Warehouse", 123), Store("Downtown Store", 124), Store("Matts Store", 12345)])
        stores_list[2].store_inventory = self.test_inventory
        yield self
        pass

    def test_get_store_success(self, setup_teardown):
        assert stores_list.get_store(12345) == stores_list[2]

    def test_get_store_failure(self, setup_teardown):
        assert stores_list.get_store(12346) is False