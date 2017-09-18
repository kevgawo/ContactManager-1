class Contact:
    def __init__(self, name="", number="", gender="", email="", postal_address=""):
        self.name = name,
        self.number = number,
        self.gender = gender,
        self.email = email,
        self.postal_address = postal_address


def add_contact():
    name = input("Your name: ")
    number = input('Your number: ')
    gender = input('Your gender (M/F>: ')
    email = input('Your email address: ')
    postal_address = input('Your postal address: ')

    contact_new = Contact(name, number, gender, email, postal_address)
    print('')
    print("Name: {}\nNumber: {}\nGender: {}\nEmail: {}\nAddress: {}\n".format(contact_new.name, contact_new.number, contact_new.gender, contact_new.email, contact_new.postal_address))

add_contact()
