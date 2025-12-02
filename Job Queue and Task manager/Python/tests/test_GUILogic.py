import pytest

class Tests:
    @pytest.fixture
    def setup_teardown(self):
        # Setup code (if needed)
        yield
        # Teardown code (if needed)

