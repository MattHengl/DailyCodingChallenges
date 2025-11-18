import JSONHandler
from ContactList import ContactList
from EmailList import EmailList
import Email

def get_action_input():
    action = input('Welcome. What would you like to do?\nCreate Card[1]\nCreate Campaign[2]\nView Campaign[3]'
                   '\nFind Campaign[4]\nDelete Campaign[5]\nSend Email[6]\nFind Contact[7]\nView all Contacts[8]\nRemove Contact[9]\nExit[0]')
    return action

def menu():
    contact_list = ContactList()
    contact_list.load_contact_list_from_memory()
    email_list = EmailList()
    email_list.load_email_list_from_memory()

    while True:
        action = get_action_input()
        if action == "1234567890" or len(action) != 1:
            print("That's not an option, sorry.")
            continue
        if action == "1":
            print("Create Contact Card")
            contact_list.add_card_to_contacts()
        if action == "2":
            print("Create Campaign")
            email_list.create_email_campaign()
        if action == "3":
            print("View Campaign")
            email_list.view_all_email_campaigns()
        if action == "4":
            print("Find Campaign")
            print(email_list.find_email_campaign())
        if action == "5":
            print("Delete Campaign")
            email_list.delete_email_campaign()
        if action == "6":
            print("Send Email")
            email_list.send_email()
        if action == "7":
            print("Find Contact")
            contact_list.find_contact(input("Enter the email address of the contact to find: "))
        if action == "8":
            print("View All Contacts")
            contact_list.view_all_contacts()
        if action == "9":
            print("Remove Contact")
            contact_list.remove_contact_card()
        if action == "0":
            print("Exiting Program")
            break

if __name__ == "__main__":
    #print(f"{EmailList.check_date_to_send_auto_email(email_list)} emails sent today automatically.")
    menu()
