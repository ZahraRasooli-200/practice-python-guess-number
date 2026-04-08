import json


class ContactManager:
    def __init__(self, path= "-"):
        self.contact_list = []

        if path != "-":
            print("loading contacts from file...")
            with open(path, 'r') as f:
                data = f.read()
                self.contact_list = json.load(data)
            print("contacts loaded successfully!")


    def add_contact(self, name, phone_number):
        self.contact_list.append({
            'name': name,
            'phone_number': phone_number
        })

    def search(self, name):
        result = []
        for contact in self.contact_list:
            if name.lower() in contact['name'].lower():
                result.append(contact)
            print(f"search result: {result}")

    def backup(self):
        with open('./contacts_backup.json', 'w') as f:
            f.write(json.dumps(self.contact_list))

    def print(self):
        print(f"your contact list: {self.contact_list}")


my_contacts = ContactManager(path = "./contacts_backup.json")
my_contacts.add_contact("Alice", "123-456-7890")
my_contacts.add_contact("Bob", "987-654-3210")
my_contacts.print()

my_contacts.search("Alice")
my_contacts.backup()