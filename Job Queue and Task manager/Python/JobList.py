from logging import raiseExceptions

from Python.Job import Job

class JobList:
    def __init__(self):
        self.job_list: list[Job] = []

    def __repr__(self):
        return f"{self.job_list}"


    def get_job_list(self):
        return self.job_list

    def get_job_size(self):
        return len(self.job_list)

    def find_job(self, job_to_find):
        if job_to_find is not None or job_to_find != "":
            for job in self.job_list:
                print(f"{job.job_name.lower().strip()} - {job_to_find.lower().strip()}")
                if job.job_name.lower() == job_to_find.lower():
                    return job
        return False
    def add_job(self, job = None):
        try:
            if job is not None:
                self.job_list.append(job)
            else:
                self.job_list.append(Job())
            return True
        except Exception as e:
            print(e)
            return False
    def remove_job(self, job = None):
        try:
            if len(self.job_list) != 0:
                if job is not None:
                    self.job_list.remove(job)
                    return True
                else:
                    raise Exception("Job object is empty")
            else:
                raise Exception("Job List is empty")
        except Exception as e:
            print(e)
            return False
    def view_jobs(self):
        try:
            if len(self.job_list) != 0:
                for job in self.job_list:
                    print(job.__str__())
                return True
            else:
                raise Exception("Job List is empty")
        except Exception as e:
            print(e)
            return False
