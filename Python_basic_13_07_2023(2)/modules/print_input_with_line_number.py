
"""
This mmodule will return the message with line number
"""
#    #method code_with_number
# def code_with_line_number()-> dict:
#     """
#     This function take  a code as(run time input) multi line string  and return 
#     a dictionary with line number as key and code as value
#     Parameters
#     ----------
#     code: str
#        string containing code
#     Return
#     str
#        return string each line with line number 
#     """
#     print("Enter your code string and for end press ctrl+z")
#     code_dictionary={}
#     line_num=1
#     while True:
#         try:
#             code_string_input=input()
#         except EOFError:
#             print("String end here")
#             break
#         code_dictionary[line_num]=code_string_input
#         line_num+=1
#     return code_dictionary

def input_code_string()-> str:
    """
    This function take  a code as(run time input) multi line string  and return 
    a string of input provided by the user
    Parameters
    ----------
    None
    Return
    str
       return string 
    """
    print("Enter your code string and for end press ctrl+z")
    code_list=[]
    while True:
        try:
            code_string_input=input()
        except EOFError:
            print("String end here")
            break
        code_list.append(code_string_input)
    return convert_code_into_line_number('\n'.join(code_list))

def convert_code_to_raw(code: str)-> str:
    """
    This function take a string as input and return a raw string
    Parameters
    ----------
    code: code
       string containing code
    Return
    str
       return string in raw format 
    """
    return fr"{code}"

def convert_code_into_line_number(code_str: str)-> None:
    """
    This function take a string as input and return each line with a 
    line number
    Parameters
    ----------
    code_str
        string containing the code
    Return
    None 
    """
    code_str_raw=convert_code_to_raw(code_str)
    output_str=code_str_raw.split('\n')
    num_count=0
    output_code_list=[]
    for line in output_str:
        num_count+=1
        output_code_list.append(str(num_count)+" "+line) 
    print('\n'.join(output_code_list))
