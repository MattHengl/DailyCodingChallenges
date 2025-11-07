import ContactCard
import EmailList
import JSONHandler
import ContactList
import Email

contact_list = ContactList.ContactList.contact_list
email_list = EmailList.EmailList.email_list

def get_action_input():
    action = input('Welcome. What would you like to do?\nCreate Card[1]\nCreate Campaign[2]\nView Campaign[3]'
                   '\nFind Campaign[4]\nDelete Campaign[5]\nSend Email[6]\nFind Contact[7]\nView all Contacts[8]\nRemove Contact[9]\nExit[0]')
    return action
def know_unique_id():
    if input("Do you know the unique ID number of the campaign? (y/n): ").lower() == "n":
        EmailList.view_all_email_campaigns(email_list)
def menu():
    while True:
        action = get_action_input()
        if action == "1234567890" or len(action) != 1:
            print("That's not an option, sorry.")
            continue
        if action == "1":
            print("Create Contact Card")
            ContactList.add_card_to_contacts(contact_list, ContactCard.get_contact_info())
            JSONHandler.save_json("Contacts.JSON", contact_list)
        if action == "2":
            print("Create Campaign")
            EmailList.create_email_campaign(email_list, Email.get_email_info())
            JSONHandler.save_json("Emails.JSON", email_list)
        if action == "3":
            print("View Campaign")
            EmailList.view_all_email_campaigns(email_list)
        if action == "4":
            print("Find Campaign")
            know_unique_id()
            print(EmailList.find_email_campaign(email_list, input("Enter the unique ID number of the campaign to find: ")))
        if action == "5":
            print("Delete Campaign")
            know_unique_id()
            EmailList.delete_email_campaign(email_list, input("Enter the unique ID number of the campaign to delete: "))
        if action == "6":
            print("Send Email")
            know_unique_id()
            EmailList.send_email(EmailList.find_email_campaign(email_list, input("Enter the unique ID number of the campaign to delete: ")), contact_list)
        if action == "7":
            print("Find Contact")
            ContactList.find_contact(contact_list, input("Enter the email address of the contact to find: "))
        if action == "8":
            print("View All Contacts")
            ContactList.view_all_contacts(contact_list)
        if action == "9":
            print("Remove Contact")
            ContactList.remove_contact_card(contact_list)
            JSONHandler.save_json("Contacts.JSON", contact_list)
        if action == "0":
            print("Exiting Program")
            break

if __name__ == "__main__":
    email_list = list((JSONHandler.load_json("Emails.JSON")))
    contact_list = list((JSONHandler.load_json("Contacts.JSON")))
    print(f"{EmailList.check_date_to_send_auto_email(email_list, contact_list)} emails sent today automatically.")
    menu()
