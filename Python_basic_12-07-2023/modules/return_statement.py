"""
This module will perform the return statement functionalities
"""
from typing import Union
   #return single value
def return_single_value(name: str)-> str:
    """
    This function take  a name as string  and return a welcome message
    Parameters
    ----------
    name: str
        name of the user
    Return
    str
        return a welcome message as string
    """
    return f"Welcome to {name}"

    #return multiple values using list
def return_multiple_using_list(name: str, age: int)-> list:
    """
    This function take  a name as string and age as int return 
    these values as list
    Parameters
    ----------
    name: str
        name of the user
    age: int
        age of the user
    Return
    list
        return a list contianing name of user and age of user
    """
    return [name, age]

    #return multiple values using dictionary
def return_multiple_using_dict(name: str, age: int, message: str)->dict:
    """
    This function take  a name as str and age as int and
    message as str and return these values as dict
    Parameters
    ----------
    name: str
        name of the user
    age: int
        age of the user
    message: str
        message for the user
    Return
    dict
        return a dictionary contianing name of user ,age of user and 
        message for user 
    """
    user_dict: dict[str, Union[str, int]]={'name': name, 'age': age, 'message':message}
    return user_dict
