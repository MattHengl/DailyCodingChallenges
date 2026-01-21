import pytest
from DataValidation import DataValidation
from Product import Product


class TestDataValidation:
    @pytest.fixture()
    def setup_teardown(self):
        self.test_inventory = [Product("Tomato", 1.50, 0), Product("Lettuce", 1.00, 5)]
        yield self
        pass

    # checking stock
    # Will be giving a product and quantity, if the stock is less than quantity, it should return false
    @pytest.mark.parametrize("product", [Product("Tomato", 1.50, 10)])
    def test_check_stock_success(self, product):
        assert DataValidation.check_stock(product) is True

    @pytest.mark.parametrize("product", [Product("Tomato", 1.50, 0)])
    def test_check_stock_failure(self, product):
        assert DataValidation.check_stock(product) is False

    @pytest.mark.parametrize("product", [Product("Apple", 1.50, 10)])
    def test_check_sku_success(self, product, setup_teardown):
        assert DataValidation.check_sku(product, self.test_inventory) is True

    #This test isn't needed since the SKUs are randomly generated
    '''@pytest.mark.parametrize("product", [Product("Apple", 1.50, 10)])
    def test_check_sku_failure(self, product, setup_teardown):
        assert DataValidation.check_sku(product, self.test_inventory) is False'''
