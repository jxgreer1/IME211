from contacts_manager_functions import add_contact, view_contact, delete_contact, show_contacts

john_doe = {'Name': 'John Doe', 'Phone Number': '555-555-1234', 'Age': 30, 'Favorite Color': 'Blue'}
jane_doe = {'Name': 'Jane Doe', 'Phone Number': '555-555-1235', 'Age': 25, 'Favorite Color': 'Orange'}
john_smith = {'Name': 'John Smith', 'Phone Number': '555-555-1236', 'Age': 35, 'Favorite Color': 'Red'}
jane_smith = {'Name': 'Jane Smith', 'Phone Number': '555-555-1237', 'Age': 45, 'Favorite Color': 'Green'}

contacts = {'John Doe': john_doe, 'Jane Doe': jane_doe, 'John Smith': john_smith, 'Jane Smith': jane_smith}


def main(contacts_library):
    user_input = ''

    while user_input != '5':
        print("Welcome to the Contacts Manager!")
        print("1. Add a contact")
        print("2. View a contact")
        print("3. Delete a contact")
        print("4. Show all contacts")
        print("5. Exit")
        user_input = input("Please select an option: ")

        if user_input == '1':
            add_contact(contacts_library)
        elif user_input == '2':
            view_contact(contacts_library)
        elif user_input == '3':
            delete_contact(contacts_library)
        elif user_input == '4':
            show_contacts(contacts_library)
        elif user_input == '5':
            exit()
        else:
            print("Invalid input. Please try again.")
            main(contacts_library)


main(contacts)
