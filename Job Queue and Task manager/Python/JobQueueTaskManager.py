from Python.app_state import job_list

# Having a system that is able to run multiple async based jobs at the same time
# Can keep a record of the things that are being ran
# Will need a way to start jobs
# Will need a way to monitor jobs
# Will need a way to log the different type of jobs
# Different type of jos(email, file process, data import, API calls)
# Sleep job, file copy job, data generator job, math calc job, random fail job
# Able to pause jobs and then restart them later, even after program has been restarted

# When the program starts, it should go through all jobs in the list and run them at the time needed
# When a job runs, it should change the status to running
# Once the job is done, then it should change the status to completed

if __name__ == '__main__':
    job_list.run_scheduled_jobs()

    from Python import JobManagerGUI
    JobManagerGUI.root.mainloop()
