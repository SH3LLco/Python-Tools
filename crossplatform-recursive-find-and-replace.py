#!/usr/bin/python3
import subprocess
import os
import platform
import time
import shutil
from fileinput import FileInput
from tkinter import filedialog as fd


# clear screen
os.system('cls' if os.name == 'nt' else 'clear')

# author tag  
tag = '''
 ████     █████                    █████       ████████            
░░███   ███░░░███                 ░░███       ███░░░░███           
 ░███  ███   ░░███ █████ ███ █████ ░███ █████░░░    ░███ █████ ████
 ░███ ░███    ░███░░███ ░███░░███  ░███░░███    ██████░ ░░███ ░███ 
 ░███ ░███    ░███ ░███ ░███ ░███  ░██████░    ░░░░░░███ ░███ ░███ 
 ░███ ░░███   ███  ░░███████████   ░███░░███  ███   ░███ ░███ ░███ 
 █████ ░░░█████░    ░░████░████    ████ █████░░████████  ░░███████ 
░░░░░    ░░░░░░      ░░░░ ░░░░    ░░░░ ░░░░░  ░░░░░░░░    ░░░░░███ 
                                                          ███ ░███ 
                                                         ░░██████  
                                                          ░░░░░░   
    ▄▀
    ▄▀            ╱╱╱╱╱╭┳━━━╮
▄▀▄▀▄▀▄▀▄▀        ╱╱╱╱╱┃┃╭━╮┃
    ▄▀            ╭━━┳━╯┃┃┃┃┃
    ▄▀            ┃╭╮┃╭╮┃┃┃┃┃
                  ┃╭╮┃╰╯┃╰━╯┃
                  ╰╯╰┻━━┻━━━╯                                                     
                                                          
Follow our Github!: 
L0WK3Y https://github.com/L0WK3Y-IAAN
ad0    https://github.com/SecurityGino                                                          
                                                          '''

# print author tag
print(tag)
time.sleep(3)

# clear screen
os.system('cls' if os.name == 'nt' else 'clear')

# try and exception handling for MacOS
try:
    
    # checking if OS is MACOS
    if (platform.system()) == 'Darwin':   
        print('MacOS Detected \n \n')       
              
        print('Checking if Homebrew is installed... \n \n')      
        time.sleep(3)

        # creates result variable of response of brew command
        result = subprocess.run(['brew --version'], capture_output=True, text=True, shell=True)

        # if result.returncode == 0: continue
        if result.returncode == 0:
            print("Homebrew is installed, continuing... \n \n")
            time.sleep(3)

        

        # else install Homebrew    
        else:
            
            print("Homebrew is not installed \n \n")
            
            print("Installing Homebrew... Press ctrl-c to cancel, continuing in 5 seconds... \n \n")
            time.sleep(5)

            # download Homebrew install.sh to file
            url_to_file = "https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh"
            output_file = "install.sh"

            # error handling
            try:
                # Download the file with curl
                subprocess.run(["curl", "-O", url_to_file])

                # Execute the downloaded script
                subprocess.run(["bash", output_file])
                

            except subprocess.CalledProcessError as e:
                print(f"Error installing Homebrew: {e} \n \n")     
        
        
        # install tkinter
        print('Installing dependency tkinter, Press ctrl-c to cancel, continuing in 5 seconds... \n \n')
        time.sleep(5)
        subprocess.call(["brew install python-tk"], shell=True)
        time.sleep(3)
        
        
            
    # continue if OS is Linux or Windows
    else:
        print('Linux or Windows Detected, continuing... \n \n')
        time.sleep(3)

   
    # define directories, print selected directories and grabs users input for string replacements
    
    print("\n \nPlease select the root directory to perform the find and replace operation \n \n")
    time.sleep(3)
    root_folder = fd.askdirectory()
    print("\n \nRoot Directory Selected: {0}\n \n \n".format(root_folder))
    time.sleep(3)
    print("\n \nPlease create or select a backup folder \n \n \n")
    time.sleep(3)
    backup_folder = fd.asksaveasfilename()
    print("\n \nBackup Directory Selected: {0}\n \n \n".format(backup_folder))
    time.sleep(3)
    old_string = input("\n \nEnter old string:")
    time.sleep(3)
    new_string = input("\n \nEnter new string:")
    time.sleep(3)


    # 
    def backup_folder_operation(root_folder, backup_folder):
        try:
            # Create a backup folder if it doesn't exist
            if not os.path.exists(backup_folder):
                os.makedirs(backup_folder)

            # Copy the contents of the source folder to the backup folder
            shutil.copytree(root_folder, os.path.join(backup_folder, os.path.basename(root_folder)))
            time.sleep(3)
            print(f"\n \nBackup of {root_folder} created successfully in {backup_folder} \n \n")
            

        except Exception as e:
            print(f"Error creating backup: {e} \n \n")
            

    backup_folder_operation(root_folder, backup_folder)
    
   

    # replace_string_in_files function requires 3 parameters to be executed
    def replace_string_in_files(root_folder, old_string, new_string):
        for (foldername, sub, files) in os.walk(root_folder, topdown=True):
            for file in files:
                filepath = os.path.join(foldername, file)

                # error handling
                try:    
                    
                    # Access the file contents and replaces the specified string
                    with open(filepath, 'rb') as f:
                        content = f.read()
                    with open(filepath, 'wb') as f:
                        f.write(content.replace(old_string.encode('utf-8'), new_string.encode('utf-8')))
                except FileNotFoundError as e:
                    print(f"File not found: {e.filename} \n \n")

    # calls the function along with required parameters
    replace_string_in_files(root_folder, old_string, new_string)
    print("Find and Replace Operation Complete! \n \n")
    time.sleep(3)
    

# except KeyboardInterrupt:
except KeyboardInterrupt:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Program Terminated...Exiting. \n \n')
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')