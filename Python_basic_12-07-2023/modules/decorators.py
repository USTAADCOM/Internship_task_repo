"""
This module will perform the different functionalities using decorators
"""
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
