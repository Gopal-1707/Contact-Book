class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {"phone": phone, "email": email, "address": address}

    def view_contacts(self):
        for name, details in self.contacts.items():
            print(f"{name}: {details['phone']} | {details['email']} | {details['address']}")

    def search_contact(self, query):
        for name, details in self.contacts.items():
            if query.lower() in name.lower() or query in details["phone"]:
                print(f"{name}: {details['phone']} | {details['email']} | {details['address']}")

    def update_contact(self, name, phone, email, address):
        if name in self.contacts:
            self.contacts[name] = {"phone": phone, "email": email, "address": address}
        else:
            print(f"{name} not found in contacts.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
        else:
            print(f"{name} not found in contacts.")


if __name__ == "__main__":
    my_contact_book = ContactBook()

    my_contact_book.add_contact("Alice", "123-456-7890", "alice@example.com", "123 Main St")
    my_contact_book.add_contact("Bob", "987-654-3210", "bob@example.com", "456 Elm St")

    my_contact_book.view_contacts()

    print("\nSearching for 'Alice':")
    my_contact_book.search_contact("Alice")

    print("\nUpdating Bob's contact:")
    my_contact_book.update_contact("Bob", "555-123-4567", "newbob@example.com", "789 Oak Ave")
    my_contact_book.view_contacts()

    print("\nDeleting Alice's contact:")
    my_contact_book.delete_contact("Alice")
    my_contact_book.view_contacts()
