from Python.Job import Job
from Python.JobList import JobList

# single shared JobList instance used by GUI and the runner
job_list = JobList()
job_list.add_job(Job("Email Matt", "email", "2025-06-01"))
job_list.add_job(Job("Sleep Job", "Sleep", "2025-06-01"))

