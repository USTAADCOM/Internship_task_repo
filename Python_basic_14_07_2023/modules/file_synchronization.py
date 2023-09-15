"""
This mmodule contain the file synchronizer.
"""
import os
import hashlib
import time
import shutil
import sys
# create_log method
def create_log(message: str)-> None:
    """
    This function will take  a message and create and create its log in 
    activity_log.txt.
    Parameters
    ----------
    message: str
    Return
    ------
    None
    """
    current_action = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open("activity_log.txt", '+a', encoding='Utf-8') as log_file:
        log_file.write('['+ current_action +']'+message+'\n')

# compare  files method
def compare_file(file_one: str, file_two: str)-> bool:
    """
    Take two file name as input and compare the contents of these files
    if not same then return False if same then return True.
    Parameters
    ----------
    file_one: str
        name of the first file.
    file_two: str
        name of the second file.
    Return
    ------
    bool
    """
    with open(file_one, 'rb') as f_one:
        with open(file_two, 'rb') as f_two:
            if hashlib.sha224(f_one.read()).hexdigest() == hashlib.sha224(f_two.read()).hexdigest():
                return True
            else:
                return False
# synchronizer method
def synchronizer(main_folder: str, folder_two: str)-> None:
    """
    synchronizer function will take folders name as input and perform 
    file synchronization between these folders.
    Parameters
    ----------
    main_folder: str
        name or path of the first folder.
    folder_two: str
        name or path of the second folder.
    Return
    ------
    None
    """
    # copy all files from main_folder in list files_in_main
    files_in_main = os.listdir(main_folder)
    # copy all files from folder_two in list files_in_two
    files_in_two = os.listdir(folder_two)

    # compare files_in_main with files_in_two
    if len(files_in_main) != len(files_in_two):
        return False

    for file_main in files_in_main:
        if file_main in files_in_two:
            abs_path_main=os.path.abspath(main_folder+'/'+file_main)
            abs_path_two=os.path.abspath(folder_two+'/'+file_main)
            if not compare_file(abs_path_main, abs_path_two):
                return False
        else:
            return False
    return True

# execute_synchronizer method
def execute_synchronizer(main_folder_path: str, folder_two_path: str)-> None:
    """
    execute_synchronizer function will take folder path as input and perform 
    file synchronization between these folders.
    Parameters
    ----------
    main_folder_path: str
        name or path of the main folder.
    folder_two_path: str
        name or path of the second folder.
    Return
    ------
    None
    """
    if os.path.isfile('config.txt'):
        print("config file: OK")
        create_log('config file: OK')
        # read folder path from config.txt
        with open("config.txt", 'r', encoding='utf-8') as f_config:
            lines = f_config.readlines()
            folder = lines[0].split('::')[1].strip()
            backup = lines[1].split('::')[1].strip()
            synchronizer(folder, backup)
    else:
        create_log('config file: NOT FOUND')
        print("config file: NOT FOUND")

        # Allow user to enter folder path
        # #  folder = input('input your main folder path:')
        # #  backup = input('input your second folder path:')
        folder = main_folder_path
        backup = folder_two_path
        # check if folder exist
        if not os.path.isdir(folder):
            create_log('folder: NOT FOUND')
            print('folder is not exist')
            sys.exit()
        # check if backup is exist
        if not os.path.isdir(backup):
            create_log('backup: NOT FOUND')
            print('backup is not exist')
            sys.exit()
        # write folder path on config.txt
        with open('config.txt', 'w', encoding='utf-8') as con_file:
            con_file.write('folder::'+folder)
            con_file.write('\n')
            con_file.write('backup::'+backup)
            print('config file: CREATED')
            create_log('config file: CREATED')
    # synchronization start with loop and keep it repeating after 10 seconds
    print("Please Press ctrl+c For End Snchronization")
    while True:
        try:
            # check if folder is same with backup
            if synchronizer(folder, backup):
                now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                print(f'[{now}] file is up to date')
                create_log('file is up to date')
                # sleep for 10 seconds
                time.sleep(10)
                continue
            # check folder exist or not
            if os.path.isdir(folder):
                print('folder: Exist')
                create_log('folder: Exist')
            else:
                print('folder is not exist')
                create_log('folder is not exist')
                print('please check your config file')
                break
            # check backup is exist or not.
            if os.path.isdir(backup):
                print('backup: Exist')
                create_log('backup: Exist')
            else:
                print('backup is not exist')
                create_log('backup is not exist')
                print('please check your config file')
                break
            # variable to count sync, update anf delete operation.
            count_sync = 0
            update_file = 0
            delete_file = 0
            # copy all files from folder in list files
            files = os.listdir(folder)
            # copy all files from backup in list files_backup
            files_backup = os.listdir(backup)
            # compare folder with bacjup
            for file in files_backup:
                if file in files:
                    if compare_file(folder+'/'+file, backup+'/'+file):
                        create_log(f'{file} is up to date')
                        count_sync += 1
                    else:
                        # copy file from folder to backup
                        update_file += 1
                        os.remove(backup+'/'+file)
                        abs_path_folder=os.path.abspath(folder+'/'+file)
                        abs_path_backup=os.path.abspath(backup+'/'+file)
                        shutil.copy(abs_path_folder, abs_path_backup)
                        create_log(f'{file} is updated')
                if file not in files:
                    # delete file in backup
                    create_log(f'{file} is deleted')
                    delete_file += 1
                    os.remove(backup+'/'+file)
            for file in files:
                if file not in files_backup:
                    # copy file from folder to backup
                    update_file += 1
                    create_log(f'{file} is copied')
                    abs_path_folder=os.path.abspath(folder+'/'+file)
                    abs_path_backup=os.path.abspath(backup+'/'+file)
                    shutil.copy(abs_path_folder, abs_path_backup)
            now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f'[{now}] sync: {count_sync}; update: {update_file}; delete: {delete_file};')
            # sleep for 10 seconds
            time.sleep(10)
        except KeyboardInterrupt:
            print("Synchronization End!")
            break
