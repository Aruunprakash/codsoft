contacts = {}

def add_contact():
    name = input("Enter contact name: ").strip()
    if name in contacts:
        print("Contact with this name already exists.")
        return
    
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()
    
    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    
    print(f"Contact {name} added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts to display.")
    else:
        print("\n--- Contact List ---")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}")
        print()


def search_contact():
    search_term = input("Enter name or phone number to search: ").strip()
    found = False
    for name, info in contacts.items():
        if search_term.lower() in name.lower() or search_term == info['phone']:
            print(f"\nContact Found: {name}")
            print(f"Phone: {info['phone']}, Email: {info['email']}, Address: {info['address']}")
            found = True
            break
    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ").strip()
    if name in contacts:
        phone = input("Enter new phone number (leave blank to keep current): ").strip()
        email = input("Enter new email (leave blank to keep current): ").strip()
        address = input("Enter new address (leave blank to keep current): ").strip()

        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        if address:
            contacts[name]['address'] = address
        
        print(f"Contact {name} updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print("Contact not found.")

def contact_book_menu():
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting contact book. Successful ")
            break
        else:
            print("Invalid choice, please try again.")

contact_book_menu()
