'''
    For the given path, get the List of all files in the directory tree 
'''
import os
from hurry.filesize import size
import csv
import pandas as pd

def get_directory_metadata(dir_path: str, log_dict: dict)-> list:
    """
    get_directory_metadata function will take folders name and empty log as input.
    
    Parameters
    ----------
    dir_path: str
        path of the folder.
    log_dict: dict
        dictionary containing the metadeta.
    
    Return
    ------
    log_dict: dict
        dictionary contain the metadata
    """
    count = 0
    total_size = 0
    file_at_path = os.listdir(dir_path)
    folder_name = os.path.basename(dir_path)
    log_dict[folder_name] = {}
    for ele in os.scandir(dir_path):
        total_size += os.path.getsize(ele)
    log_dict[folder_name]['folder_size'] = size(total_size)
    # Iterate over all the files in directory
    for file in file_at_path:
        full_path = os.path.join(dir_path, file)
        # If entry is a file then get the store its metadata
        if os.path.isfile(full_path):
            count+=1
            log_dict[folder_name]['file_name'+str(count)] = file
            log_dict[folder_name]['file_size'+str(count)] = size(os.path.getsize(os.path.abspath(dir_path+'/'+file)))
        else:
            log_dict = get_directory_metadata(full_path, log_dict)
    return log_dict

# generate_summary method
def generate_summary(log_dict: dict)-> None:
    """
    generate_summary function will take dict as input and generate metadata
    summry.
    
    Parameters
    ----------
    log_dict: dict
        metadata dictionary.

    Return
    ------
    None
    """
    with open('log.txt', 'w', encoding='utf-8') as con_file:
        for folder_name, data_dict in log_dict.items():
            # df_data = pd.DataFrame(log_dict)
            # df_data.to_csv("log.csv")
            # con_file.write(folder_name)
            print("__________________________________")
            for key, data in data_dict.items():
                print(f"{key} :{log_dict[folder_name][key]}")
                con_file.write("\n")
                con_file.write(f"{key} :{log_dict[folder_name][key]}")
            con_file.write("\n")
        con_file.close()
# main_synchronizer method
def main_synchronizer(dir_path: str)-> None:
    """
    main_synchronizer function will take folders name as input.
    
    Parameters
    ----------
    dir_path: str
        path of the folder.

    Return
    ------
    None
    """
    log_dict={}
    metadat_dict = get_directory_metadata(dir_path, log_dict)
    generate_summary(metadat_dict)
# import matplotlib.pyplot as plt

# data = {'milk': 60, 'water': 10}
# names = list(data.keys())
# values = list(data.values())

# plt.bar(range(len(data)), values, tick_label=names)
# plt.show()

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
        header = ['File Name', 'File Size']
        dic_writer=csv.DictWriter(file, fieldnames = header)
        dic_writer.writeheader()
        for key, value in phone_book.items():
            temp_dict={'Phone':key, 'Name':value}
            dic_writer.writerow(temp_dict)
