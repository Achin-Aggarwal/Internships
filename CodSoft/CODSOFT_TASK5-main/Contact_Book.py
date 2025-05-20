import json
import csv
import re

# File to store contacts
CONTACTS_FILE = 'contacts.json'
CSV_FILE = 'contacts.csv'

def load_contacts():
    try:
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def is_valid_phone(phone):
    return re.match(r'^\+?\d{10,15}$', phone) is not None

def is_valid_email(email):
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email) is not None

def add_contact(contacts):
    name = input("Enter the contact's name: ").strip()
    phone = input("Enter the contact's phone number: ").strip()
    if not is_valid_phone(phone):
        print("Invalid phone number format.")
        return
    email = input("Enter the contact's email: ").strip()
    if not is_valid_email(email):
        print("Invalid email address format.")
        return
    address = input("Enter the contact's address: ").strip()
    
    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    print(f"Contact '{name}' added successfully.")

def view_contacts(contacts, sort_by_name=False):
    if not contacts:
        print("No contacts available.")
        return

    if sort_by_name:
        contacts = dict(sorted(contacts.items()))

    print("\n--- Contact List ---")
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}")

def search_contact(contacts):
    search_term = input("Enter the name or phone number to search: ").strip()
    
    results = {name: info for name, info in contacts.items() 
               if search_term.lower() in name.lower() or search_term in info['phone']}
    
    if not results:
        print("No contacts found.")
        return
    
    print("\n--- Search Results ---")
    for name, info in results.items():
        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}, Address: {info['address']}")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ").strip()
    
    if name not in contacts:
        print("Contact not found.")
        return
    
    print("Leave fields empty to keep the current value.")
    
    phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ").strip()
    if phone and not is_valid_phone(phone):
        print("Invalid phone number format.")
        return
    email = input(f"Enter new email (current: {contacts[name]['email']}): ").strip()
    if email and not is_valid_email(email):
        print("Invalid email address format.")
        return
    address = input(f"Enter new address (current: {contacts[name]['address']}): ").strip()
    
    if phone:
        contacts[name]['phone'] = phone
    if email:
        contacts[name]['email'] = email
    if address:
        contacts[name]['address'] = address
    
    print(f"Contact '{name}' updated successfully.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()
    
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print("Contact not found.")

def export_contacts_to_csv(contacts):
    with open(CSV_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Phone', 'Email', 'Address'])
        for name, info in contacts.items():
            writer.writerow([name, info['phone'], info['email'], info['address']])
    print(f"Contacts exported to {CSV_FILE}.")

def import_contacts_from_csv(contacts):
    try:
        with open(CSV_FILE, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['Name']
                contacts[name] = {
                    'phone': row['Phone'],
                    'email': row['Email'],
                    'address': row['Address']
                }
        print(f"Contacts imported from {CSV_FILE}.")
    except FileNotFoundError:
        print(f"{CSV_FILE} not found. Please make sure the file exists.")

def main():
    contacts = load_contacts()
    
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Export Contacts to CSV")
        print("7. Import Contacts from CSV")
        print("8. Exit")
        
        choice = input("Choose an option (1-8): ").strip()
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            sort_option = input("Sort contacts by name? (yes/no): ").strip().lower()
            view_contacts(contacts, sort_by_name=(sort_option == 'yes'))
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            export_contacts_to_csv(contacts)
        elif choice == '7':
            import_contacts_from_csv(contacts)
        elif choice == '8':
            save_contacts(contacts)
            print("Exiting the contact book. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
