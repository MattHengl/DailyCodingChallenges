import pytest
from Python import Job
from Python import JobList

class Tests:

    job_list = JobList.JobList()

    test_email_job = [
        (Job.Job("Email Matt", "email", "2025-06-01 10:00:00", "pending"), True)
    ]

    @pytest.fixture
    def setup_teardown(self):
        # Setup code (if needed)
        Tests.job_list.add_job(Job.Job("Email Matt", "email", "2025-06-01 10:00:00", "pending"))
        Tests.job_list.add_job(Job.Job("Sleep for 10", "sleep", "2025-06-01 10:00:00", "pending"))
        Tests.job_list.add_job(Job.Job("Copy File", "file", "2025-06-01 10:00:00", "pending"))
        Tests.job_list.add_job(Job.Job("Generate Fake Data", "data", "2025-06-01 10:00:00", "pending"))
        Tests.job_list.add_job(Job.Job("Some Math Function", "math", "2025-06-01 10:00:00", "pending"))
        Tests.job_list.add_job(Job.Job("Job to fail", "random", "2025-06-01 10:00:00", "pending"))
        yield
        # Teardown code (if needed)

    @pytest.mark.asyncio
    async def test_run_email(self):
        assert await Job.run_email() is True

    @pytest.mark.parametrize("job, exception", test_email_job)
    @pytest.mark.asyncio
    async def test_run_file_copy(self, job, exception):
        assert await Job.run_file_copy(job) is exception