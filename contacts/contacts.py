import json


def load_contacts():

    try:

        with open("contacts.json", "r") as file:

            return json.load(file)

    except FileNotFoundError:

        return {}


def save_contacts(contacts):

    with open("contacts/contacts.json", "w") as file:

        json.dump(contacts, file, indent=4)


def add_contact(contacts):

    name = input("Enter name: ")

    phone = input("Enter phone: ")

    email = input("Enter email: ")


    contacts[name] = {"phone": phone, "email": email}

def view_contacts(contacts):

    if not contacts:

        print("No contacts found.")

        return


    for name, info in contacts.items():

        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")


def search_contact(contacts):


    name = input("Enter name to search: ")

    if name in contacts:

        info = contacts[name]

        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

    else:

        print("Contact not found.")


def delete_contact(contacts):

    name = input("Enter name to delete: ")

    if name in contacts:

        del contacts[name]

        print("Contact deleted.")

    else:

        print("Contact not found.")