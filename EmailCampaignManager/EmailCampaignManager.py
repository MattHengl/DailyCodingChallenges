import Email
import EmailerInfo
import JSONHandler

def adds(x,y):
    return x + y
def get_action_input():
    action = input('Welcome. What would you like to do?\nCreate Email[1]\nCreate Card[2]\nCreate Campaign[3]\nView '
                   'Campaign[4]\nDelete Campaign[5]\nSend Email[6]\nFind Contact[7]\nView all Contacts[8]')
    return action
def menu():
    while True:
        action = get_action_input()
        if action == "123456" or len(action) != 1:
            print("That's not an option, sorry.")
            continue
        if action == "1":
            print("Create Email")
            Email.create_email()
        if action == "2":
            print("Create Card")
            EmailerInfo.create_emailer_card()
        if action == "3":
            print("Create Campaign")
            Email.create_email_campaign()
        if action == "4":
            print("View Campaign")
            Email.view_email_campaign()
        if action == "5":
            print("Delete Campaign")
            Email.delete_email_campaign()
        if action == "6":
            print("Send Email")
            Email.send_email()
        if action == "7":
            print("Find Contact")
            EmailerInfo.find_contact(contactList)
        if action == "8":
            print("View All Contacts")
            EmailerInfo.view_all_contacts(contactList)


emailList = JSONHandler.load_json("Emails.JSON")
contactList = JSONHandler.load_json("Contacts.JSON")
#menu()
