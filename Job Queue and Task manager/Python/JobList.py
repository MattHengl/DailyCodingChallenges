from Python import Job

class JobList:
    job_list: list[Job.Job] = []

    def add_job(self, job: Job.Job) -> bool:
        try:
            if job is not None:
                self.job_list.append(job)
                return True
            else:
                raise Exception("Job object is empty")
        except Exception as e:
            print(e)
            return False
    def remove_job(self, job: Job.Job) -> bool:
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
