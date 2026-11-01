from contacts import (
    load_contacts,
    save_contacts,
    add_contact,
    view_contacts,
    search_contact,
    delete_contact
)


def main():

    contacts = load_contacts()

    while True:

        print("\n--- Contact Manager ---")

        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Select option: ")

        if choice == "1":

            add_contact(contacts)
            save_contacts(contacts)
            

        elif choice == "2":

            view_contacts(contacts)

        elif choice == "3":

            search_contact(contacts)

        elif choice == "4":

            delete_contact(contacts)
            save_contacts(contacts)

        elif choice == "5":

            save_contacts(contacts)

            print("Contacts saved. Goodbye!")

            break

        else:

            print("Invalid option")


main()