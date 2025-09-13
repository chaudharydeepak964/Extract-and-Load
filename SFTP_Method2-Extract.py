#!/usr/bin/env python
# coding: utf-8


print(" ** Welcome Report on BI Portal with 2nd Method ** ")


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


path = r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\NEC_I\RAW'

for folder, subfolders ,files in os.walk(path):
    for fl in files:
        if fl.endswith(".csv" )or fl.endswith('.xlsx'):
            path = os.path.join(folder, fl)
            os.remove(path)

print("All Old Raw Files Deleted!")


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



                                   ###########   *********************** QOS DOWNLAODING  ***********************  #############





print(" ** QOS Files downloading start ** ")

ssh0=paramiko.SSHClient()
ssh0.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh0.connect(hostname='1.1.1.1',username='admin',password='admin',port=22)
except:
    pass

try:
    ssh0.connect(hostname='10.10.10.10',username='admin',password='admin',port=22)
except:
    pass

sftp_client0=ssh0.open_sftp()

print(" ** Host Connected ** ")


print('Files Downloaded from 1st Path')

inbound_files1 = []

try:
    source_folder1 = 'Remote_Directory_Path'+d1+'/' 
    local_folder1 = r'Local_Path'
    inbound_files1 = sftp_client0.listdir(source_folder1)
    print(inbound_files1)
except Exception as e:
    print(f"Error occurred while fetching the list of files: {e}")
    
if inbound_files1:
    for ele1 in inbound_files1:
        try:
            if ('IDUQOS_VR4_VR10_'+dd1+'') in ele1:
                path_from = source_folder1 + '/' + ele1
                path_to = local_folder1 + '/'+ ele1
                sftp_client0.get(path_from, path_to)

                new_filename = 'New_Name-IDUQOS_VR4_VR10_'+dd1+'_2.2.2.2_Daily.csv'  
                new_path = os.path.join(local_folder1, new_filename)
            
                # Rename the file
                os.rename(path_to, new_path)
            
                print(f"File {ele1} downloaded and renamed to {new_filename}")
        except Exception as e:
            print(f"Error occurred while processing file {ele1}: {e}")
            
else:
    print("No files to download.")

    

for ele1 in inbound_files1:
    try:
        if ('IDUQOS_'+dd1+'') in ele1:
            path_from = source_folder1 + '/' + ele1
            path_to = local_folder1 + '/'+ ele1
            sftp_client0.get(path_from, path_to)

            new_filename = 'New_Name-IDUQOS_'+dd1+'_3.3.3.3_Daily.csv'  
            new_path = os.path.join(local_folder1, new_filename)
            
            # Rename the file
            os.rename(path_to, new_path)
               
            print(f"File {ele1} downloaded and renamed to {new_filename}")
            
    except:
        print(ele1)


# ************************************************************** New Path ********************************************

print('Files Downloaded from 1st Path')

try:
    source_folder1 = 'Remote_Directory_Path2/'+d1+'/' 
    local_folder1 = r'Destination_Path2'
    inbound_files1 = sftp_client0.listdir(source_folder1)
    print(inbound_files1)
except:
    pass

for ele1 in inbound_files1:
    try:
        if ('IDUQOS_VR4_VR10_'+dd1+'') in ele1:
            path_from = source_folder1 + '/' + ele1
            path_to = local_folder1 + '/'+ ele1
            sftp_client0.get(path_from, path_to)

            new_filename = 'New_Name-IDUQOS_VR4_VR10_'+dd1+'_4.4.4.4_Daily.csv'  
            new_path = os.path.join(local_folder1, new_filename)
            
            # Rename the file
            os.rename(path_to, new_path)

            print(f"File {ele1} downloaded and renamed to {new_filename}")
            
    except:
        print(ele1)



for ele1 in inbound_files1:
    try:
        if ('IDUQOS_'+dd1+'') in ele1:
            path_from = source_folder1 + '/' + ele1
            path_to = local_folder1 + '/'+ ele1
            sftp_client0.get(path_from, path_to)

            new_filename = 'New_Name-IDUQOS_'+dd1+'_4.4.4.4_Daily.csv'  
            new_path = os.path.join(local_folder1, new_filename)
            
            # Rename the file
            os.rename(path_to, new_path)
                      
            print(f"File {ele1} downloaded and renamed to {new_filename}")
            
    except:
        print(ele1)



print ( " QOS Duplicate files deleted : IF 0KB Files Downloaded " )

path = r'\Local_Directory_Path\'

for folder, subfolders,files in os.walk(path):
    for fl in files:
        if fl.startswith("IDUQOS_VR4" ):
            path = os.path.join(folder, fl)
            os.remove(path)

print(" * Duplicate Files Deleted! * ")


path = r'\Local_Directory_Path2\'

for folder, subfolders,files in os.walk(path):
    for fl in files:
        if fl.startswith("ETH_REPORT" ):
            path = os.path.join(folder, fl)
            os.remove(path)

print(" * Delete 0 Kb file! * ")

