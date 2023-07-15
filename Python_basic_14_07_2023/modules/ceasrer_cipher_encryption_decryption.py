"""
This mmodule will perform the encryption and decryption on a file content
   using ceaser cipher technique.
"""
   #method caesar_cipher_encryption
def caesar_cipher_encryption(real_text: str, step: int)-> list:
    """
    This function will take  a text string , step as input and return
    a list of encrypted text using ceaser cipher.
    Parameters
    ----------
    real_text: str
       string containing the original text.
    step: int
        containing the step for encryption.
    Return
    ------
    list
        return a list of encrypted text.
    """
    output_text_list = []
    encrypt_text_list = []
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'
	            , 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'
		        , 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for str_letter in real_text:
        if str_letter in uppercase:
            index = uppercase.index(str_letter)
            encryting_text = (index + step) % 26
            encrypt_text_list.append(encryting_text)
            new_char = uppercase[encryting_text]
            output_text_list.append(new_char)
        elif str_letter in lowercase:
            index = lowercase.index(str_letter)
            encryting_text = (index + step) % 26
            encrypt_text_list.append(encryting_text)
            new_char = lowercase[encryting_text]
            output_text_list.append(new_char)
        else:
            output_text_list.append(str_letter)
    return output_text_list

# method caesar_cipher_decnryption
def caesar_cipher_decnryption(real_text: str, step: int)-> list:
    """
    This function will take  a text string , step as input and return
    a list of decrypted text using ceaser cipher. 
    Parameters
    ----------
    real_text: str
       string containing the decrypted text.
    step: int
        containing the step use for encryption.
    Return
    list
        return a list of decrypted text.
    """
    output_text_list = []
    decrypt_text_list = []
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'
	            , 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'
		        , 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for str_letter in real_text:
        if str_letter in uppercase:
            index = uppercase.index(str_letter)
            encryting_text = (index - step) % 26
            decrypt_text_list.append(encryting_text)
            new_char = uppercase[encryting_text]
            output_text_list.append(new_char)
        elif str_letter in lowercase:
            index = lowercase.index(str_letter)
            encryting_text = (index - step) % 26
            decrypt_text_list.append(encryting_text)
            new_char = lowercase[encryting_text]
            output_text_list.append(new_char)
        else:
            output_text_list.append(str_letter)
    return output_text_list

#read file content method
def read_file_content(file_name: str)-> str:
    """
    This function wil take a file name as input read its content and written
    its content as string.
    Parameters
    ----------
    file_name: str
       filename name as string.
    Return
    ------
    str
        return a string of file content.
    """
    input_str=[]
    try:
        with open(file_name, 'r', encoding='Utf-8') as file:
            input_str=file.readlines()
    except FileNotFoundError as f_n:
        print("Something wrong while opening the data"+str(f_n))
    finally:
        file.close()
    return ''.join(input_str)

# write_file_content method
def write_file_content(file_name: str, encryted_str: str)-> None:
    """
    This function wil take a file name and string as input and write the string content
    on a file.
    Parameters
    ----------
    file_name: str
       filename name as string.
    encrypted_str: str
        str contain the encrypted text.
    Return
    ------
    None
    """
    try:
        with open(file_name, 'w', encoding='Utf-8') as file:
            file.write(encryted_str)
    except FileNotFoundError as f_n:
        print("Something wrong while opening the data"+str(f_n))
    finally:
        file.close()
