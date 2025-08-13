'''
This code is built on the principle of inheritance.
The code have two parents which are Phone and Camera and have one child which is Smartphone.
The parent Phone saves new contacts only and can remove them and call them if the contact exists.
The parent Camera saves pics that user takes.
'''
class Phone:
    def __init__(self):
        self.contacts=[]

    def add_contact(self,name):

        name = name.strip().title()
        '''
        This is for when the user enters a space at the beginning or end of the name.
        And also capitalizes the first letter of each word.
        So if the user saves alice and wants to call Alice, it will work.
        '''
        if name not in self.contacts: # Here the code check if the name already exists in the user contacts or not.
            self.contacts.append(name)
            print(f"Contact '{name}' added successfully")
        else:
            print("Contact already exists")

    def remove_contact(self,name):

        name = name.strip().title()
        if name in self.contacts: # Here the code check if the name exists in the user contacts or not.
            self.contacts.remove(name)
            print(f"Contact '{name}' removed successfully")
        else:
            print("Contact not found")

    def make_call(self,name):

        name = name.strip().title()
        if name in self.contacts: # Here the code check if the name exists in the user contacts or not.
            print("Calling "+name)
        else:
            print("Contact not found")
class Camera:
    def take_pic(self):
        print("The picture was taken successfully")
class Smartphone(Phone,Camera):
    pass