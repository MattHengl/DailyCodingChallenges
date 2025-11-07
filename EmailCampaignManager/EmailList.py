import datetime
import Email
import smtplib
from email.message import EmailMessage
import random

class EmailList:
    email_list: list[Email.Email] = []

    def __repr__(self):
        return f"{self.email_list}"

def create_email_campaign(email_list, email_info):
    try:
        if email_list is not None and email_info is not None:
            if find_email_campaign(email_list, email_info.ID) != {}:
                email_info.ID = random.randint(1, 9999)
            email_list.append(email_info)
        else:
            raise Exception("Contact card is invalid.")
        return True
    except Exception as e:
        print(f"Error: {e} on line {e.__traceback__.tb_lineno}")
        return False

def view_all_email_campaigns(email_list):
    if len(email_list) > 0:
        for email in email_list:
            print(f"{email}")
        return True
    else:
        print("Email Campaign List is Empty")
        return False

def find_email_campaign(email_list, id_to_find):
    if len(email_list) > 0:
        for email in email_list:
            email_id = email.get('ID') if isinstance(email, dict) else getattr(email, 'ID', None)
            if email_id == int(id_to_find):
                return email
        else:
            print("Was not able to find the email campaign you were looking for.")
            return {}
    else:
        print("Email Campaign List is Empty")
        return {}

def delete_email_campaign(email_list, id_to_delete):
    email_to_remove = find_email_campaign(email_list, id_to_delete)
    email_list.remove(email_to_remove if email_to_remove != {} else None)
    return True

def check_date_to_send_auto_email(email_list, contact_list):
    emails_sent = 0
    if len(email_list) > 0:
        current_date = datetime.datetime.now()
        for email in email_list:
            if email.get('send_date') == current_date.strftime("%m/%d/%Y"):
                # send_email(email, contact_list)
                emails_sent += 1
    else:
        print("There are no email campaigns in the email list.")
    return emails_sent


def send_email(email_info, contact_list):
    try:
        if len(contact_list) > 0:
            if email_info is not None:
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