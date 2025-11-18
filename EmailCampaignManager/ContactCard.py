class Contact:
    def __init__(self, firstname = None, lastname = None, email = None, company = None):
        self.firstname = firstname if firstname is not None else self.set_firstname()
        self.lastname = lastname if lastname is not None else self.set_lastname()
        self.email = email if email is not None else self.set_email()
        self.company = company if company is not None else self.set_company()
    def __str__(self):
        return f"\n{self.firstname} {self.lastname} | {self.email} | {self.company}\n"

    def set_firstname(self):
        while not (first_name := input("Enter your first name: ")).strip():
            print("Can not be blank.")
        return first_name

    def set_lastname(self):
        while not (last_name := input("Enter your last name: ")).strip():
            print("Can not be blank.")
        return last_name

    def set_email(self):
        while not (email := input("Enter your email: ")).strip():
            print("Can not be blank.")
        return email

    def set_company(self):
        while not (company := input("Enter your company: ")).strip():
            print("Can not be blank.")
        return company

    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname

    def get_email(self):
        return self.email

    def get_company(self):
        return self.company