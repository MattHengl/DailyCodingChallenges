class Contact:
    def __init__(self, firstname, lastname, email, company):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.company = company
    def __str__(self):
        return f"\n{self.firstname} {self.lastname} | {self.email} | {self.company}\n"

def get_contact_info():
    firstname = input("Enter the first name of the contact: ")
    lastname = input("Enter the last name of the contact: ")
    email = input("Enter the email address of the contact: ")
    company = input("Enter the company of the contact: ")
    return Contact(firstname, lastname, email, company)