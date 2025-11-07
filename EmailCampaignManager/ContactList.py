import ContactCard

class ContactList:
    contact_list: list[ContactCard.Contact] = []

def add_card_to_contacts(contact_list, contact_card):
    try:
        if contact_list is not None and contact_card is not None:
            contact_list.append(contact_card)
        else:
            raise Exception("Contact card is invalid.")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def remove_contact_card(contact_list, contact_card=None):
    try:
        if contact_card is None:
            contact = find_contact(contact_list, input("Enter the email address of the contact to find: "))
            if not contact:
                return False
            contact_list.remove(contact)
            return True
        if contact_card in contact_list:
            contact_list.remove(contact_card)
            return True
        return False
    except Exception as e:
        print(f"Error removing contact: {e}")
        return False

def find_contact(contact_list, email_to_find):
    try:
        for contact in contact_list:
            email = contact.get('email') if isinstance(contact, dict) else getattr(contact, 'email', None)
            if email == email_to_find:
                print(contact)
                return contact
        raise Exception("Contact not found.")
    except Exception as e:
        print(f"Error: {e}")
        return False

def view_all_contacts(contact_list):
    for contact in contact_list:
        print(f"{contact}")