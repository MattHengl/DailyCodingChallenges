from Python import JobList
from Python import Job
import pytest

class Tests:
    job_list = JobList.JobList()

    test_job = [
        (Job.Job("Email Matt", "email", "2025-06-01 10:00:00", "pending"), True)
    ]
    @pytest.mark.parametrize("job,expected", test_job)
    def test_add_job(self, job, expected):
        assert Tests.job_list.add_job(job) is expected
    def test_add_job_empty_job(self):
        assert Tests.job_list.add_job(None) is False

    @pytest.mark.parametrize("job,expected", test_job)
    def test_remove_job(self, job, expected):
        assert Tests.job_list.remove_job(job) is expected
    def test_remove_job_empty_job(self):
        assert Tests.job_list.remove_job(None) is False
    @pytest.mark.parametrize("job, expected", test_job)
    def test_remove_job_empty_list(self, job, expected):
        assert Tests.job_list.remove_job(job) is False
    @pytest.mark.parametrize("job,expected", test_job)
    def test_remove_job_cant_find_job(self, job, expected):
        Tests.job_list.add_job(job)
        assert Tests.job_list.remove_job(Job.Job("Email Lori", "email", "2025-06-01 10:00:00", "pending")) is False

    def test_view_jobs(self):
        assert Tests.job_list.view_jobs() is True
    def test_view_jobs_empty_list(self):
        Tests.job_list.job_list = []
        assert Tests.job_list.view_jobs() is False
