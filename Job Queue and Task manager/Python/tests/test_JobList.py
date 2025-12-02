import datetime

from Python.JobList import JobList
from Python import Job
import pytest

class Tests:
    @pytest.fixture
    def setup_teardown(self):
        # Setup code (if needed)
        self.test_job_list = JobList()
        self.test_job_list.add_job(Job.Job("Email Matt", "email", "2025-06-01"))
        yield
        # Teardown code (if needed)

    test_job = [
        (Job.Job("Sleep Job", "job", "2025-06-01"), True)
    ]
    @pytest.mark.parametrize("job,expected", test_job)
    def test_add_job(self, setup_teardown, job, expected):
        assert self.test_job_list.add_job(job) is expected
    def test_add_job_empty_job(self, setup_teardown, monkeypatch):
        inputs = ["Sleep Job", "Sleep", datetime.datetime.now().strftime("%m/%d/%Y")]
        input_iterator = iter(inputs)
        monkeypatch.setattr("builtins.input", lambda _: next(input_iterator))
        assert self.test_job_list.add_job() is True

    @pytest.mark.parametrize("job,expected", test_job)
    def test_remove_job(self, setup_teardown, job, expected):
        self.test_job_list.add_job(job)
        assert self.test_job_list.remove_job(job) is expected
    def test_remove_job_empty_job(self, setup_teardown):
        assert self.test_job_list.remove_job() is False
    @pytest.mark.parametrize("job, expected", test_job)
    def test_remove_job_empty_list(self, setup_teardown, job, expected):
        assert self.test_job_list.remove_job(job) is False
    @pytest.mark.parametrize("job,expected", test_job)
    def test_remove_job_cant_find_job(self, setup_teardown, job, expected):
        assert self.test_job_list.remove_job(Job.Job("Email Lori", "email", "2025-06-01")) is False
    @pytest.mark.parametrize("job,expected", test_job)
    def test_view_jobs(self, setup_teardown, job, expected):
        assert self.test_job_list.view_jobs() is True
    def test_view_jobs_empty_list(self, setup_teardown):
        self.test_job_list.job_list = []
        assert self.test_job_list.view_jobs() is False
    @pytest.mark.parametrize("job,expected", test_job)
    def test_find_job(self, setup_teardown, job, expected):
        self.test_job_list.add_job(job)
        assert self.test_job_list.find_job(job.job_name) is job
    @pytest.mark.parametrize("job,expected", test_job)
    def test_find_job_empty_string(self, setup_teardown, job, expected):
        self.test_job_list.add_job(job)
        assert self.test_job_list.find_job("") is False
