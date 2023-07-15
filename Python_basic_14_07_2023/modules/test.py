"""
This mmodule contain the contact mamangement system.
"""
   #method create_contact method
def create_contact(user_name: str, contact: str, phone_book: dict)-> dict:
    """
    This function will take user_name, contact number as string and phone_book
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
    dict
        return a dictionary containg the user phone numbers.
    """
    phone_book[contact] = user_name
    return phone_book

def delete_contact(contact: str, phone_book: dict)-> dict:
    """
    This function will take phone number and dictionary as input and return 
    dictionary after delete the user with contact.
    Parameters
    ----------
    phone: str
        containing the user contact.
    phone_book: dict
        containing the user contacts
    Return
    ------
    dict
        return a dictionary containg the user phone numbers."""
    if contact in phone_book:
        phone_book.pop(contact)
    else:
        print("Contact not found")
    return phone_book

def display_contact(phone_book: dict)-> None:
    """
    This function will take dictionary as input and return 
    dictionary with user contact.
    Parameters
    ----------
    phone_book: dict
        containing the user contacts
    Return
    ------
    dict
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
        string containing user contact
    phone_book: 
        containing the user contacts
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
        string containing user contact
    edited_phone:
        string containing new phone number
    phone_book: 
        containing the user contacts
    Return
    ------
    phone_book: dict
        containing the user contacts 
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

def welcome_function(phone_book: dict)-> None:
    """
    This function will take the dictionary as input and provide all the 
    functionalities for phone book management.
    Parameters
    ----------
    phone_book: dict
    
    ------
    None"""
    while True:
        # phone_book_updated={}
        print("1. Add new contact")
        print("2. Search contact")
        print("3.Display contact")
        print("4. Edit contact")
        print("5. Delete contact")
        print("6.Exit")
        choice = int(input("Enter your choice"))
        if choice == 1:
            name = input("enter the contact name ")
            phone = input("enter the mobile number")
            phone_book=create_contact(name, phone, phone_book)
            print(phone_book)
        elif choice == 2:
            search_contact_num = input("enter the contact for search")
            search_contact(search_contact_num, phone_book)
        elif choice == 3:
            if not phone_book:
                print("empty phone book")
            else:
                display_contact(phone_book)
        elif choice == 4:
            contact = input("Enter the contact to be edited")
            new_contact = input("Enter the new contact")
            update_contact(contact, new_contact, phone_book)
        elif choice == 5:
            del_contact = input("Enter the contact to be deleted ")
            if del_contact in phone_book:
                confirm = input("Do you want to delete this contact y/n? ")
                if confirm =='y' or confirm =='Y':
                    phone_book.pop(del_contact)
                    display_contact(phone_book)
                else:
                    print("Name is not found in contact book")
        else:
            break
