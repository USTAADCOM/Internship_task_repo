"""
import modules from modules folder
"""
from modules import print_input_with_line_number as line_num

#main function

def main():
    """
    For the execution of modules
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
    #print(typing_library.division(numerator=2, denominator=3))
    #print(typing_library.division(numerator=6, denominator=3))
    #print(typing_library.division(numerator=2, denominator=0)) #rise error

    # call method print_input_with_line_number() method
    input_str=r"""def print(s):
    print(f"this is your string\n{s}")"""
    line_num.input_code_string() 
if __name__=='__main__':
    main()
