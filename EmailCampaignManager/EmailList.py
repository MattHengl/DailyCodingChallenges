import datetime
from Email import Email
from email.message import EmailMessage
import JSONHandler

class EmailList:
    def __init__(self):
        self.email_list: list[Email] = []

    def __repr__(self):
        return f"{self.email_list}"

    def create_email_campaign(self, email_info = None):
        try:
            if email_info is None:
                print("Lets create a new email campaign to add to the email list!")
                email_to_add = Email()
                self.check_ID(email_to_add)
                self.email_list.append(email_to_add)
            else:
                print("Adding email campaign to the email list.")
                self.email_list.append(email_info)
            return True
        except Exception as e:
            print(f"Error: {e} on line {e.__traceback__.tb_lineno}")
            return False
        finally:
            JSONHandler.save_json("Emails.JSON", self.email_list)

    def check_ID(self, email_to_add):
        while email_to_add in self.email_list:
                print("That ID is already in the email list. Giving it a new ID")
                email_to_add.set_ID()

    def view_all_email_campaigns(self):
        if len(self.email_list) > 0:
            for email in self.email_list:
                print(f"{email}")

    def find_email_campaign(self, id_to_find = None):
        try:
            if len(self.email_list) > 0:
                if id_to_find is None:
                    self.know_unique_id()
                    id_to_find = input("Enter the unique ID number of the email campaign to find: ")
                for email in self.email_list:
                    email_id = email.get('ID') if isinstance(email, dict) else getattr(email, 'ID', None)
                    if email_id == int(id_to_find):
                        return email
            else:
                raise Exception("Email_list is empty.")
        except Exception as e:
            print(f"Error: {e}")
            return {}


    def delete_email_campaign(self, id_to_delete = None):
        try:
            if len(self.email_list) > 0:
                email_to_remove = self.find_email_campaign(id_to_delete)
                self.email_list.remove(email_to_remove if email_to_remove != {} else None)
                return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            JSONHandler.save_json("Emails.JSON", self.email_list)

    def check_date_to_send_auto_email(self):
        emails_sent = 0
        if len(self.email_list) > 0:
            current_date = datetime.datetime.now()
            for email in self.email_list:
                if email.get_send_date() == current_date.strftime("%m/%d/%Y"):
                    # send_email(email, ContactList.get_list())
                    emails_sent += 1
        else:
            print("There are no email campaigns in the email list.")
        return emails_sent


    def send_email(self, contact_list, email_info = None):
        try:
            if len(contact_list) > 0:
                if email_info is None:
                    email_info = self.find_email_campaign()
                msg = EmailMessage()
                msg.set_content(f"{email_info.content}\n\nClick here: {email_info.url}")
                msg['Subject'] = email_info.subject
                msg['From'] = email_info.sender
                for contact in contact_list:
                    if email_info.sending_audience.lower() == "all":
                        msg['To'] = contact.email
                        print("EMAIL SENT")
                        #with smtplib.SMTP('localhost') as s:
                            #s.send_message(msg)
                    else:
                        category, value = email_info.sending_audience.split("-", 1)
                        contact_value = (contact.get(category.lower()) if isinstance(contact, dict) else getattr(contact, category.lower(), None))
                        if contact_value == value:
                            msg['To'] = contact.email
                            print("EMAIL SENT")
                            #with smtplib.SMTP('localhost') as s:
                                #s.send_message(msg)
                    return True
                else:
                    raise Exception("Email_info is empty.")
            else:
                raise Exception("Contact_list is empty.")

        except Exception as e:
            print(f"Error sending email: {e} on line {e.__traceback__.tb_lineno}")
            return False

    def know_unique_id(self):
        if input("Do you know the unique ID number of the campaign? (y/n): ").lower() == "n":
            self.view_all_email_campaigns()

    def load_email_list_from_memory(self):
        self.email_list = list((JSONHandler.load_json("Emails.JSON")))