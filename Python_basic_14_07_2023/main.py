"""
import modules from modules folder.
"""
# from modules import ceasrer_cipher_encryption_decryption as ced
from modules import contact_mangement_system as cms
# from modules import file_synchronization as fs
# from modules import ransomeware

#main function

def main():
    """
    For the execution of modules.
    Parameters
    ----------
    None
    Return
    ------
    None
    """
# str_input = ced.read_file_content("test_original_file.txt")
# step = 2

# #encrytion
# encrpted_output=ced.caesar_cipher_encryption(str_input, step)
# ced.write_file_content('test_decryption.txt', ''.join(encrpted_output))

# #decrytion
# str_encryt_output = ced.read_file_content("test_decryption.txt")
# decrpted_output = ced.caesar_cipher_decnryption(str_encryt_output, step)
# ced.write_file_content('test_encrytion.txt', ''.join(decrpted_output))

# Contact management system
cms.welcome_function('contacts_csv.csv')

# Synchronizer execution
# fs.execute_synchronizer('C:/Users/AL RAFIO/Desktop/test_first',
#                      'C:/Users/AL RAFIO/Desktop/test_second')
# fs.synchronizer('C:/Users/AL RAFIO/Desktop/test_first',
#                      'C:/Users/AL RAFIO/Desktop/test_second')

# ransomeware.encryption('E:/Ekkel AI task practice/Python_basic_14_07_2023/modules/ransom_testing')
# ransomeware.decryption('E:/Ekkel AI task practice/Python_basic_14_07_2023/modules/ransom_testing')

if __name__=='__main__':
    main()
