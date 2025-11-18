from ContactCard import Contact
import JSONHandler

class ContactList:
    def __init__(self):
        self.contact_list: list[Contact] = []

    def is_empty(self):
        if len(self.contact_list) == 0:
            return True
        else:
            return False

    def get_list(self):
        return self.contact_list

    def add_card_to_contacts(self, contact_card = None):
        try:
            if contact_card is None:
                print("Lets create a new contact to add to the list!")
                self.contact_list.append(Contact())
            else:
                print("Adding contact to list.")
                self.contact_list.append(contact_card)
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            JSONHandler.save_json("Contacts.JSON", self.contact_list)

    def remove_contact_card(self, contact_card=None):
        try:
            if len(self.contact_list) > 0:
                if contact_card is None:
                    contact = self.find_contact(input("Enter the email address of the contact to find: "))
                    if not contact:
                        raise Exception("Contact not found.")
                    print(f"Removing {contact}")
                    self.contact_list.remove(contact)
                    return True
                if contact_card in self.contact_list:
                    print(f"Removing {contact_card}")
                    self.contact_list.remove(contact_card)
                    return True
            else:
                raise Exception("Contact List is empty.")
        except Exception as e:
            print(f"Error removing contact: {e}")
            return False
        finally:
            JSONHandler.save_json("Contacts.JSON", self.contact_list)

    def find_contact(self, email_to_find):
        print(f"Trying to find {email_to_find}")
        try:
            for contact in self.contact_list:
                email = contact.get('email') if isinstance(contact, dict) else getattr(contact, 'email', None)
                if email == email_to_find:
                    print(contact)
                    return contact
            raise Exception("Contact not found.")
        except Exception as e:
            print(f"Error: {e}")
            return False

    def view_all_contacts(self):
        if len(self.contact_list) > 0:
            for contact in self.contact_list:
                print(f"{contact}")

    def load_contact_list_from_memory(self):
        self.contact_list = list((JSONHandler.load_json("Contacts.JSON")))