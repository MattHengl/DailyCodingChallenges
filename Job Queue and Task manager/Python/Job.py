import asyncio
import random
from email.message import EmailMessage
import shutil
from lorem_text import lorem

class Job:
    source_file = "CopyFrom.txt"
    destination_file = "CopyTo.txt"

    def __init__(self, job_name = None, job_type = None, scheduled_run_time = None):
        self.job_name = job_name if job_name is not None else self.set_job_name()
        self.job_type = job_type if job_type is not None else self.set_job_type()
        self.scheduled_run_time = scheduled_run_time if scheduled_run_time is not None else self.set_scheduled_run_time()
        self.status = "Pending"

    def __str__(self):
        return (f"\nJob Name:{self.job_name}\n"
                f"Job Type: {self.job_type}\n"
                f"Job Run Time: {self.scheduled_run_time}\n"
                f"Job Status: {self.status}")

    def set_job_name(self, job_name = None):
        if job_name is not None:
            self.job_name = job_name
        else:
            while not (job_name := input("Enter Job Name: ").strip()):
                print("Job Name cannot be empty. Please enter a valid Job Name.")
            self.job_name = job_name
    def set_job_type(self, job_type = None):
        if job_type is not None:
            self.job_type = job_type
        else:
            while not (job_type := input("Enter Job Type: ").strip()):
                print("Job Type cannot be empty. Please enter a valid Job Type.")
            self.job_type = job_type
    def set_scheduled_run_time(self, scheduled_run_time = None):
        if scheduled_run_time is not None:
            self.scheduled_run_time = scheduled_run_time
        else:
            while not (scheduled_run_time := input("Enter Scheduled Run Time (YYYY-MM-DD): ").strip()):
                print("Scheduled Run Time cannot be empty. Please enter a valid Scheduled Run Time.")
            self.scheduled_run_time = scheduled_run_time

    async def run_job(self):
        if self.job_type.lower().__contains__("email"):
            await run_email()
        if self.job_type.lower().__contains__("sleep"):
            await run_sleep()
        if self.job_type.lower().__contains__("file"):
            await run_file_copy(self.source_file, self.destination_file)
        if self.job_type.lower().__contains__("data"):
            await run_data_generator(self.source_file)
        if self.job_type.lower().__contains__("math"):
            await run_math_job()
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
async def run_file_copy(source_path, destination_path):
    try:
        shutil.copyfile(source_path, destination_path)
        print(f"File '{source_path}' copied to '{destination_path}' successfully.")
        with open(destination_path, "r") as f:
            content = f.read()
            print(f"Content of '{destination_path}': {content}")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
async def run_data_generator(path):
    try:
        with open(path, "w") as f:
            paragraphs = lorem.paragraphs(int(input("How many paragraphs of lorem ipsum would you like to generate?")))
            f.write(paragraphs)
            return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
async def run_math_job():
    try:
        x = 2#random.randint(1, 100)
        y = 2#random.randint(1, 100)
        interation_amount = 3#random.randint(1, 100)
        for _ in range(interation_amount):
            print(f"{pow(x, y)}")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
async def run_random_fail():
    try:
        check = random.randint(0, 100)
        if check >= 50:
            return True
        else:
            raise Exception("Random number was less than 50")
    except Exception as e:
        print(f"Error: {e}")
        return False