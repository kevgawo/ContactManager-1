class ContactManager:
    def __init__(self, contacts=[]):
        self.contacts = contacts

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully")

    def search_contact(self, name=''):
        name = input('Enter name to search: ')
        for contact in self.contacts:
            if contact.name == name:
                return print(contact.name, contact.age, contact.number, contact.gender)
            else:
                return print('Sorry {} is not found in contact'.format(name))

    def delete_contact(self, name=''):
        name = input('Enter name to delete: ')
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return print('Contact removed successfully')
            else:
                return print('Sorry {} is not found in contact'.format(name))

    def get_contacts(self):
        for contact in self.contacts:
            print(contact.name, contact.number, contact.age, contact.gender)
        else:
            return print('Sorry no contact found')


class Contact:
    def __init__(self, name='', age='', number='', gender=''):
        self.name = input('Your name: ')
        self.number = input('Your number: ')
        self.age = input('Your age: ')
        self.gender = input('Your gender: ')


def main():

    while True:
        new_contact = ContactManager()
        ans = int(input('Press 1 to add, 2 to search, 3 to delete and 4 to fetch all contacts: '))

        if ans == 1:
            contact = Contact()
            new_contact.add_contact(contact)
        elif ans == 2:
            new_contact.search_contact()
        elif ans == 3:
            new_contact.delete_contact()
        elif ans == 4:
            new_contact.get_contacts()
        else:
            print('Sorry bye bye')
            break

main()