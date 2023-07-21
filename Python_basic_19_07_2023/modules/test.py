'''
    For the given path, get the List of all files in the directory tree 
'''
import os

import csv
# import pandas as pd

def get_directory_metadata(dir_path: str, log_dict: dict)-> dict:
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
    folder_total_size = 0
    file_at_path = os.listdir(dir_path)
    folder_name = os.path.basename(dir_path)
    for ele in os.scandir(dir_path):
        folder_total_size += os.path.getsize(ele)
    # Iterate over all the files in directory
    file_list = []
    for file in file_at_path:
        full_path = os.path.join(dir_path, file)
        # If entry is a file then get the store its metadata
        if os.path.isfile(full_path):
            empty_list = []
            file_size = os.path.getsize(os.path.abspath(dir_path+'/'+file))
            empty_list.append(folder_name)
            empty_list.append(int(folder_total_size/1024))
            empty_list.append(file)
            name, extension = os.path.splitext(file)
            empty_list.append(extension)
            if file_size/1024 < 1024:
                empty_list.append(round(file_size/1024, 2))
                empty_list.append("KB")
            else:
                empty_list.append(round(file_size/(1024*1024), 2))
                empty_list.append("MB")
            file_list.append(empty_list)
            log_dict[dir_path] = file_list
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
            con_file.write("_________________________________")
            con_file.write("\n")
            con_file.write(folder_name)
            for log_list in data_dict:
                con_file.write("\n")
                con_file.write(f"{log_list}")
            con_file.write("\n")
        con_file.close()
    write_csv(log_dict)

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
    file_log_dict = get_directory_metadata(dir_path, log_dict)
    generate_summary(file_log_dict)


def write_csv(log_dict: dict)-> None:
    """
    Function will read data from log_dict dictionary and store it in csv file.
    
    Parameters
    ----------
    log_dict: 
        containing the files and folders record.
    Return
    ------
    None
    """
    header = ['Folder Name', 'Folder Size(KB)', 'File Name', 'File Extension', 'File Size(KB)', 'Unit']
    with open("log_csv.csv", 'w', newline='', encoding='utf-8') as file:
        list_writer=csv.writer(file)
        list_writer.writerow(header)
        for folder_name, data_dict in log_dict.items():
            for log_list in data_dict:
                list_writer.writerow(log_list)
        file.close()
