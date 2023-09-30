class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def update_contact(self, new_name, new_phone, new_email, new_address):
        self.name = new_name
        self.phone = new_phone
        self.email = new_email
        self.address = new_address

    def display_contact(self):
        print(f"Name: {self.name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")
        print(f"Address: {self.address}")
class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for i, contact in enumerate(self.contacts, 1):
                print(f"Contact {i}: {contact.name}, Phone: {contact.phone}")

    def search_contacts(self, query):
        results = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone:
                results.append(contact)
        return results

    def update_contact(self, contact_index, new_name, new_phone, new_email, new_address):
        contact = self.contacts[contact_index]
        contact.update_contact(new_name, new_phone, new_email, new_address)

    def delete_contact(self, contact_index):
        del self.contacts[contact_index]
class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for i, contact in enumerate(self.contacts, 1):
                print(f"Contact {i}: {contact.name}, Phone: {contact.phone}")

    def search_contacts(self, query):
        results = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone:
                results.append(contact)
        return results

    def update_contact(self, contact_index, new_name, new_phone, new_email, new_address):
        contact = self.contacts[contact_index]
        contact.update_contact(new_name, new_phone, new_email, new_address)

    def delete_contact(self, contact_index):
        del self.contacts[contact_index]
def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")

            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)
            print("Contact added successfully!")

        elif choice == "2":
            contact_book.view_contacts()

        elif choice == "3":
            query = input("Enter name or phone number to search: ")
            results = contact_book.search_contacts(query)
            if results:
                print("Search results:")
                for i, result in enumerate(results, 1):
                    print(f"Result {i}:")
                    result.display_contact()
            else:
                print("No matching contacts found.")

        elif choice == "4":
            contact_index = int(input("Enter the index of the contact to update: "))
            if 0 <= contact_index < len(contact_book.contacts):
                new_name = input("Enter new name: ")
                new_phone = input("Enter new phone: ")
                new_email = input("Enter new email: ")
                new_address = input("Enter new address: ")
                contact_book.update_contact(contact_index, new_name, new_phone, new_email, new_address)
                print("Contact updated successfully!")
            else:
                print("Invalid contact index.")

        elif choice == "5":
            contact_index = int(input("Enter the index of the contact to delete: "))
            if 0 <= contact_index < len(contact_book.contacts):
                contact_book.delete_contact(contact_index)
                print("Contact deleted successfully!")
            else:
                print("Invalid contact index.")

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
