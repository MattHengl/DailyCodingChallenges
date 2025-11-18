import random

class Email:
    def __init__(self, sender = None, subject = None, content = None, url = None, send_date = None, sending_audience = None):
        self.ID = self.set_ID()
        self.sender = sender if sender is not None else self.set_sender()
        self.subject = subject if subject is not None else self.set_subject()
        self.content = content if content is not None else self.set_content()
        self.url = url if url is not None else self.set_url()
        self.url_clicks = 0
        self.send_date = send_date if send_date is not None else self.set_send_date()
        self.sending_audience = sending_audience if sending_audience is not None else self.set_sending_audience()
    def __str__(self):
        return (f"\nID: {self.ID}\n"
                f"From: {self.sender}\n"
                f"Subject: {self.subject}\n"
                f"Content: {self.content}\n"
                f"URL: {self.url}\n"
                f"URL Clicks: {self.url_clicks}\n"
                f"Send Date: {self.send_date}\n"
                f"Sending Audience: {self.sending_audience}\n")

    def set_ID(self):
        return random.randint(1, 9999)
    def set_sender(self):
        while not ((sender := input("Enter the sender's email address: ").strip()) and "@" in sender):
            print("Invalid email address — must be non-blank and contain '@'")
        return sender
    def set_subject(self):
        while not (subject := input("Enter the email subject: ").strip()):
            print("Subject cannot be blank.")
        return subject
    def set_content(self):
        while not (content := input("Enter the email content: ").strip()):
            print("Content cannot be blank.")
        return content
    def set_url(self):
        while not (url := input("Enter the URL to be included in the email: ").strip()):
            print("URL cannot be blank.")
        return url
    def set_send_date(self):
        while not (send_date := input("Enter the date in which you want to send this campaign (MM/DD/YYYY): ")):
            print("Send date cannot be blank.")
        return send_date
    def set_sending_audience(self):
        while not (sending_audience := input(
                "What category do you want to send this email out to? (All/FirstName/LastName/Company/Email): ").strip()) or sending_audience not in [
            "All", "FirstName", "LastName", "Company", "Email"]:
            print("Invalid option. Please choose from (All/FirstName/LastName/Company/Email).")
        if sending_audience != "All":
            sending_audience = sending_audience + "-" + input(
                "Please enter in the specific value for the category you selected: ")
        return sending_audience

    def get_ID(self):
        return self.ID
    def get_sender(self):
        return self.sender
    def get_subject(self):
        return self.subject
    def get_content(self):
        return self.content
    def get_url(self):
        return self.url
    def get_send_date(self):
        return self.send_date
    def get_sending_audience(self):
        return self.sending_audience