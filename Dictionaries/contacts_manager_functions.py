def add_contact(contacts_library):
    # Prompt the user for the contact's name, phone number, age, and favorite color
    name = input("Enter the contact's name: ")
    phone_number = input("Enter the contact's phone number: ")
    age = input("Enter the contact's age: ")
    favorite_color = input("Enter the contact's favorite color: ")

    new_contact = {
        'Name': name,
        'Phone Number': phone_number,
        'Age': age,
        'Favorite Color': favorite_color
    }

    contacts_library[name] = new_contact
    print(f"Contact {name} added successfully!")

    return None


def view_contact(contacts_library):
    # Prompt the user for the contact's name, then display the contact's contact card
    user_name = input("Who would you like to find? ")

    if user_name in contacts_library:
        contact = contacts_library[user_name]
        print("---------------------------")
        print("\nContact Details:")
        print(f"Name: {contact['Name']}")
        print(f"Phone Number: {contact['Phone Number']}")
        print(f"Age: {contact['Age']}")
        print(f"Favorite Color: {contact['Favorite Color']}")
        print("---------------------------")
    else:
        print(f" '{user_name}' was not found :(")

    return None


def delete_contact(contacts_library):
    # Prompt the user for the contact's name, then delete the contact from the contact library
    deletedperson = input("Who would you like to banish?")


    if deletedperson in contacts_library:
        del contacts_library[deletedperson]
        print(f"'{deletedperson}' is gone!")

    else:
        print(f" '{deletedperson}' does not exist")
    return None


def show_contacts(contacts_library):
    # Display all contacts in the contact library
    for name in contacts_library:

        print(name)


    return None

