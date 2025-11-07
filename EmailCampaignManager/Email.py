import random

class Email:
    def __init__(self, ID, sender, subject, content, url, send_date, sending_audience):
        self.ID = ID
        self.sender = sender
        self.subject = subject
        self.content = content
        self.url = url
        self.url_clicks = 0
        self.send_date = send_date
        self.sending_audience = sending_audience
    def __str__(self):
        return (f"\nID: {self.ID}\n"
                f"From: {self.sender}\n"
                f"Subject: {self.subject}\n"
                f"Content: {self.content}\n"
                f"URL: {self.url}\n"
                f"URL Clicks: {self.url_clicks}\n"
                f"Send Date: {self.send_date}\n"
                f"Sending Audience: {self.sending_audience}\n")

def get_email_info():
    while not ((sender := input("Enter the sender's email address: ").strip()) and "@" in sender):
        print("Invalid email address — must be non-blank and contain '@'")
    while not (subject := input("Enter the email subject: ").strip()):
        print("Subject cannot be blank.")
    while not (content := input("Enter the email content: ").strip()):
        print("Content cannot be blank.")
    while not (url := input("Enter the URL to be included in the email: ").strip()):
        print("URL cannot be blank.")
    while not (send_date := input("Enter the date in which you want to send this campaign (MM/DD/YYYY): ").strip()):
        print("Send date cannot be blank.")
    while not (sending_audience := input("What category do you want to send this email out to? (All/FirstName/LastName/Company/Email): ").strip()) or sending_audience not in ["All", "FirstName", "LastName", "Company", "Email"]:
        print("Invalid option. Please choose from (All/FirstName/LastName/Company/Email).")
    if sending_audience != "All":
        sending_audience = sending_audience + "-" + input("Please enter in the specific value for the category you selected: ")
    ID = random.randint(1, 9999)
    return Email(ID, sender, subject, content, url, send_date, sending_audience)