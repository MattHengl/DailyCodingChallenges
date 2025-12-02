import datetime
import io
import pytest
from Python.Job import Job
import Python.Job

class Tests:
    @pytest.fixture
    def setup_teardown(self):
        # Setup code (if needed)
        self.test_job = Job("Email Matt", "email", datetime.datetime.now().strftime("%m/%d/%Y"))
        yield
        # Teardown code (if needed)

    @pytest.mark.asyncio
    async def test_run_email(self, setup_teardown):
        assert await Python.Job.run_email() is True

    @pytest.mark.asyncio
    async def test_run_file_copy(self, setup_teardown):
        assert await Python.Job.run_file_copy("Python/CopyFrom.txt", "Python/CopyTo.txt") is True

    @pytest.mark.asyncio
    async def test_run_data_generator(self, setup_teardown, monkeypatch):
        monkeypatch.setattr("sys.stdin", io.StringIO("3"))
        assert await Python.Job.run_data_generator("Python/CopyFrom.txt") is True

    @pytest.mark.asyncio
    async def test_run_math_job(self, setup_teardown):
        assert await Python.Job.run_math_job() is True

    @pytest.mark.asyncio
    async def test_run_random_fail(self, setup_teardown):
        assert await Python.Job.run_random_fail() is True