class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }
        self.contacts.append(contact)
        print(f"Contact '{name}' added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. {contact['name']} - {contact['phone']}")

    def search_contacts(self, keyword):
        results = [
            contact for contact in self.contacts
            if keyword.lower() in contact['name'].lower() or keyword in contact['phone']
        ]
        if not results:
            print("No matching contacts found.")
        else:
            print("\nSearch Results:")
            for contact in results:
                self.display_contact(contact)

    def update_contact(self, contact_index, name=None, phone=None, email=None, address=None):
        if 0 <= contact_index < len(self.contacts):
            contact = self.contacts[contact_index]
            contact['name'] = name if name else contact['name']
            contact['phone'] = phone if phone else contact['phone']
            contact['email'] = email if email else contact['email']
            contact['address'] = address if address else contact['address']
            print(f"Contact '{contact['name']}' updated successfully!")
        else:
            print("Invalid contact number.")

    def delete_contact(self, contact_index):
        if 0 <= contact_index < len(self.contacts):
            removed_contact = self.contacts.pop(contact_index)
            print(f"Contact '{removed_contact['name']}' deleted successfully!")
        else:
            print("Invalid contact number.")

    def display_contact(self, contact):
        print(f"\nName: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}\n")

def display_menu():
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contacts")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    contact_book = ContactBook()

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            name = input("Enter Name: ").strip()
            phone = input("Enter Phone Number: ").strip()
            email = input("Enter Email: ").strip()
            address = input("Enter Address: ").strip()
            contact_book.add_contact(name, phone, email, address)
        
        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            keyword = input("Enter name or phone number to search: ").strip()
            contact_book.search_contacts(keyword)

        elif choice == '4':
            contact_book.view_contacts()
            try:
                contact_index = int(input("Enter the contact number to update: ")) - 1
                print("Leave fields empty to keep current value.")
                name = input("Enter new name: ").strip()
                phone = input("Enter new phone number: ").strip()
                email = input("Enter new email: ").strip()
                address = input("Enter new address: ").strip()
                contact_book.update_contact(contact_index, name, phone, email, address)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '5':
            contact_book.view_contacts()
            try:
                contact_index = int(input("Enter the contact number to delete: ")) - 1
                contact_book.delete_contact(contact_index)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
