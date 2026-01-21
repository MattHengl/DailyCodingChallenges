import pytest
from Product import Product
from Reporting import Reporting


class TestReporting:
    @pytest.fixture()
    def setup_teardown(self):
        self.test_inventory = [
            Product("Tomato", 1.50, 0),
            Product("Lettuce", 1.00, 5),
            Product("Watermelon", 3.00, 10)
        ]
        yield self
        pass

    def test_current_stock_success(self, setup_teardown):
        assert Reporting.current_stock(self.test_inventory) is True
    def test_current_stock_failure(self):
        assert Reporting.current_stock([]) is False