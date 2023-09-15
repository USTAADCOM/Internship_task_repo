"""
This mmodule contain the contact mamangement system.
"""
import csv
   #method create_contact method
def create_contact(user_name: str, contact: str, phone_book: dict)-> dict:
    """
    function will take user_name, contact number as string and phone_book
    as dictionary and return dictionary.
    dictionary.
    Parameters
    ----------
    user_name: str
       string containing the user name.
    phone: str
        containing the user contact.
    phone_book: dict
        dictionary containing the user contacts
    Return
    ------
    phone_book: dict
        return a dictionary containg the user phone numbers.
    """
    phone_book[contact] = user_name
    return phone_book

def delete_contact(contact: str, phone_book: dict)-> dict:
    """
    function will take phone number and dictionary as input and return 
    dictionary after delete the user with contact.
    Parameters
    ----------
    phone: str
        containing the user contact.
    phone_book: dict
        containing the user contacts
    Return
    ------
    phone_book: dict
        return a dictionary containg the user phone numbers."""
    phone_book.pop(contact)
    return phone_book

def display_contact(phone_book: dict)-> None:
    """
    function will take dictionary as input and return 
    dictionary with user contact.
    Parameters
    ----------
    phone_book: dict
        containing the user contacts
    Return
    ------
    phone_book: dict
        return a dictionary containg the user phone numbers."""
    if not phone_book:
        print("Contact book empty")
    else:
        for key, value in phone_book.items():
            print(f"Phone Numer:{key} Name:{value}")

def search_contact(phone: str, phone_book: dict)-> None:
    """
    This function will take phone and dictionary as input and return 
    return user with match phone and name.
    Parameters
    ----------
    phone:
        string containing user contact.
    phone_book: 
        containing the user contacts.
    Return
    ------
    None
    """
    if phone in phone_book:
        print(f"Phone Numer:{phone} Name:{phone_book[phone]}")
    else:
        print("User not found")

def update_contact(phone: str, phone_edited: str, phone_book: dict)-> dict:
    """
    This function will take phone, edited phone and dictionary and update the 
    contact with new contact.
    Parameters
    ----------
    phone:
        string containing user contact.
    edited_phone:
        string containing new phone number.
    phone_book: 
        containing the user contacts.
    Return
    ------
    phone_book: dict
        containing the user contacts.
    """
    if phone in phone_book:
        contact_name=phone_book[phone]
        phone_book.pop(phone)
        phone_book[phone_edited]=contact_name
        print("contact updated")
        display_contact(phone_book)
    else:
        print("User not found")
    return phone_book


def find_contact(phone: str, phone_book: dict)-> bool:
    """
    This function will take phone and dictionary as input and return
    True or False if contact exist or not.
    Parameters
    ----------
    phone:
        string containing user contact.
    phone_book: 
        containing the user contacts.
    Return
    ------
    bool
    """
    if phone in phone_book:
        return True
    else:
        return False

def read_csv(file_name: str)-> dict:
    """
    Function will read data from csv file and store it in dictionary
    and return it.
    
    Parameters
    ----------
    file_path:
        string containing file name.
    
    Return
    ------
    contact_book: dict
        return the contact_book dictionary conatining the
        contacts saved in csv file.
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        dic_reader=csv.DictReader(file)
        phone_book={}
        for row in dic_reader:
            phone_book[row['Phone']]=row['Name']
    return phone_book


def write_csv(phone_book: dict)-> None:
    """
    Function will read data from dictionary and store it in csv file.
    
    Parameters
    ----------
    phone_book: 
        containing the user contacts.
    Return
    ------
    None
    """
    with open("contacts_csv.csv", 'w', newline='', encoding='utf-8') as file:
        fields=["Phone","Name"]
        dic_writer=csv.DictWriter(file, fieldnames=fields)
        dic_writer.writeheader()
        for key, value in phone_book.items():
            temp_dict={'Phone':key, 'Name':value}
            dic_writer.writerow(temp_dict)


def welcome_function(file_name: str)-> None:
    """
    This function will take the dictionary as input and provide all the 
    functionalities for phone book management.
    
    Parameters
    ----------
    phone_book: dict
        containing the user contacts.
    
    Return
    ------
    None
    """
    phone_book=read_csv(file_name)
    try:
        while True:
            # Chices for the user
            print('''
                    1. Add new contact
                    2. Search contact:
                    3. Display contact:
                    4. Edit contact:
                    5. Delete contact:
                    6. Exit:''')
            choice = int(input("Enter your choice: "))
            match choice:
            # Add contact
                case 1:
                    name = input("enter the contact name: ")
                    phone = input("enter the mobile number: ")
                    create_contact(name, phone, phone_book)
                case 2:
                    search_contact_num = input("enter the contact for search: ")
                    search_contact(search_contact_num, phone_book)
                case 3:
                    display_contact(phone_book)
                case 4:
                    contact = input("Enter the contact to be edited: ")
                    new_contact = input("Enter the new contact: ")
                    update_contact(contact, new_contact, phone_book)
                case 5:
                    del_contact = input("Enter the contact to be deleted: ")
                    find_result=find_contact(del_contact, phone_book)
                    if find_result:
                        confirm = input("Do you want to delete this contact y/n? ")
                        if confirm =='y' or confirm =='Y':
                            print(f"Phone Numer:{del_contact} Name:{phone_book[del_contact]} \
                              deleted Sucessfully")
                            phone_book=delete_contact(del_contact, phone_book)
                    else:
                        print("Contact not found ")
                case _:
                    print("Please enter number between 1 and 5")
                    write_csv(phone_book)
                    break
    except ValueError:
        print("Value Error")
