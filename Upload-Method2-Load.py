
#!/usr/bin/env python
# coding: utf-8

print(" ** Welcome here to Push All Reports on BI Portal ** ")


from datetime import datetime, timedelta,date
import pandas as pd
import numpy as np
import paramiko
import os.path
from datetime import date 
from os import path
from glob import glob
import glob
import errno
import shutil
import warnings
warnings.filterwarnings("ignore")

pd.set_option('display.float_format', '{:.2f}'.format)

d=int()
d0=(datetime.now() - timedelta(days=0)).strftime('%Y-%m-%d')
d1=(datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
d2=(datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d')
d3=(datetime.now() - timedelta(days=3)).strftime('%Y-%m-%d')
d4=(datetime.now() - timedelta(4)).strftime('%Y-%m-%d')
d5=(datetime.now() - timedelta(5)).strftime('%Y-%m-%d')
d6=(datetime.now() - timedelta(6)).strftime('%Y-%m-%d')

print(d1)
print(d2)
print(d3)
print(d4)
print(d5)
print(d6)


## **** For Past Month **** ##

mnt1=((datetime.now() - timedelta(1)).strftime("%Y%m%d"))
mnt1=((datetime.now() - timedelta(days =datetime.now().day)).strftime("%m-%y"))


print('Raw files Loading....')


d=int()
dd0=(datetime.now() - timedelta(days=0)).strftime('%Y%m%d')
dd1=(datetime.now() - timedelta(days=1)).strftime('%Y%m%d')
dd2=(datetime.now() - timedelta(days=2)).strftime('%Y%m%d')
dd3=(datetime.now() - timedelta(days=3)).strftime('%Y%m%d')
dd4=(datetime.now() - timedelta(4)).strftime('%Y%m%d')
dd5=(datetime.now() - timedelta(5)).strftime('%Y%m%d')
dd6=(datetime.now() - timedelta(6)).strftime('%Y%m%d')

print(dd1)
print(dd2)
print(dd3)
print(dd4)
print(dd5)
print(dd6)





                                                            # ** Reports Uploading start **   

print(" ** Reports Uploading start on BI Portal -->> /home/snenrc/VIL_IDEA_REPORTS/TX_REPORT ** ")

print(" ** Uploading Start ** ")

        

import paramiko
import os

def upload_files(local_path, remote_path, hostname, port, username, password):
    # Create an SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        # Connect to the SFTP server
        ssh.connect(hostname, port=port, username=username, password=password)
    except Exception as e:
        print(f"Failed to connect to {hostname}: {e}")
        return
    
    # Open an SFTP session
    sftp = ssh.open_sftp()
    
    try:
        # Upload files
        for root, _, files in os.walk(local_path):
            for file_name in files:
                local_file_path = os.path.join(root, file_name)
                relative_path = os.path.relpath(local_file_path, local_path)
                remote_file_path = os.path.join(remote_path, relative_path).replace("\\", "/")  # Ensure Unix-style paths
                
                # Ensure remote directory exists
                remote_dir = os.path.dirname(remote_file_path)
                try:
                    sftp.chdir(remote_dir)
                except IOError:
                    # Directory does not exist, create it
                    sftp.mkdir(remote_dir)
                    sftp.chdir(remote_dir)
                
                # Upload file
                try:
                    sftp.put(local_file_path, remote_file_path)
                    print(f"Uploaded {local_file_path} to {remote_file_path}")
                except Exception as e:
                    print(f"Failed to upload {local_file_path}: {e}")

    finally:
        # Close the SFTP session and SSH connection
        sftp.close()
        ssh.close()



# Define your parameters
local_directory = r'\Local_Directory'
remote_directory = '\Remote_Directory'
hostname = '10.10.10.10'
port = 22  # or the port your server uses
username = 'root'
password = 'root'

# Call the function to upload files
upload_files(local_directory, remote_directory, hostname, port, username, password)

print(" ** Congratulation QOS Report Uploaded ** ")

print('This is 2nd Methid to upload all Rweport at once from local to Remote Directory')