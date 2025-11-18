import asyncio
from email.message import EmailMessage
import shutil
from lorem_text import lorem

class Job:
    def __init__(self, job_name, job_type, scheduled_run_time, status):
        self.Job_name = job_name
        self.job_type = job_type
        self.scheduled_run_time = scheduled_run_time
        self.status = status

    def __str__(self):
        return (f"\nJob Name:{self.Job_name}\n"
                f"Job Type: {self.job_type}\n"
                f"Job Run Time: {self.scheduled_run_time}\n"
                f"Job Status: {self.status}")
    async def run_job(self):
        if self.job_type.lower().__contains__("email"):
            await run_email()
        if self.job_type.lower().__contains__("sleep"):
            await run_sleep()
        if self.job_type.lower().__contains__("file"):
            await run_file_copy(self)
        if self.job_type.lower().__contains__("data"):
            await run_data_generator(self)
        if self.job_type.lower().__contains__("math"):
            await run_math_job(self)
        if self.job_type.lower().__contains__("random"):
            await run_random_fail()

async def run_email():
    try:
        msg = EmailMessage()
        msg.set_content("TEST CONTENT")
        msg['Subject'] = "TEST SUBJECT"
        msg['From'] = "mhengl@gmail.com"
        msg['To'] = "mattHengl21@gmail.com"
        print("EMAIL SENT")
        # with smtplib.SMTP('localhost') as s:
        # s.send_message(msg)
        return True
    except Exception as e:
        print(e)
        return False
async def run_sleep():
    await asyncio.sleep(10)
async def run_file_copy(job: Job):
    source_file = "Python/CopyFrom.txt"
    destination_file = "Python/CopyTo.txt"
    try:
        shutil.copyfile(source_file, destination_file)
        print(f"File '{source_file}' copied to '{destination_file}' successfully.")
        with open(destination_file, "r") as f:
            content = f.read()
            print(f"Content of '{destination_file}': {content}")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
async def run_data_generator(job: Job):
    with open("Python/CopyFrom.txt", "r") as f:
        paragraphs = lorem.paragraphs(int(input("How many paragraphs of lorem ipsum would you like to generate?")))
        f.write(paragraphs)
async def run_math_job(job: Job):
    pass
async def run_random_fail():
    pass

def get_info():
    while not (job_name := input("Enter Job Name: ").strip()):
        print("Job Name cannot be empty. Please enter a valid Job Name.")
    while not (job_type := input("Enter Job Type: ").strip()):
        print("Job Type cannot be empty. Please enter a valid Job Type.")
    while not (scheduled_run_time := input("Enter Scheduled Run Time (YYYY-MM-DD): ").strip()):
        print("Scheduled Run Time cannot be empty. Please enter a valid Scheduled Run Time.")
    while not (status := input("Enter Job Status: ").strip()):
        print("Job Status cannot be empty. Please enter a valid Job Status.")
    return Job(job_name, job_type, scheduled_run_time, status)