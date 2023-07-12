"""
import modules from modules folder
"""
from modules import return_statement
from modules import typing_library

#main function

def main():
    """
    Function work as the part application will run from here
    Parameters
    ----------
    None
    Return
    ------
    None
    """
    #call return_single_value method
    name='Aamir Shail'
    print(return_statement.return_single_value(name))

    #call return_multiple_using_list method
    name='Aamir Shail'
    age=25
    print(return_statement.return_multiple_using_list(name=name, age=age))

    #call return_multiple_using_dict method
    name='Aamir Shail'
    age=25
    message="Hello Aamir! How are you?"
    print(return_statement.return_multiple_using_dict(name=name, age=age, message=message))

    #call return_optional_value method
    user_income=2000000
    print(typing_library.return_optional_value(user_income))

    #call division method
    print(typing_library.division(numerator=2, denominator=3))
    print(typing_library.division(numerator=6, denominator=3))
    print(typing_library.division(numerator=2, denominator=0)) #rise error
if __name__=='__main__':
    main()
