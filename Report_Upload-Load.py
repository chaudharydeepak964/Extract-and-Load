#!/usr/bin/env python
# coding: utf-8

print(" ** Welcome here to Push Ceragon Report on BI Portal ** ")


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
import warnings
warnings.filterwarnings("ignore")

pd.set_option('display.float_format', '{:.2f}'.format)

d1=(datetime.now() - timedelta(3)).strftime('%m-%d-%Y')

de=((datetime.now() - timedelta(1)).strftime('%d-%m-%Y'))
de0=((datetime.now() - timedelta(0)).strftime('%d-%m-%Y'))

d=(datetime.now() - timedelta(1)).strftime('%d%m%Y')
dep=((datetime.now() - timedelta(1)).strftime("%d_%b'%Y"))
mnt=((datetime.now() - timedelta(0)).strftime("%m-%y"))


## **** For Past Month **** ##

mnt1=((datetime.now() - timedelta(1)).strftime("%Y%m%d"))
mnt1=((datetime.now() - timedelta(days =datetime.now().day)).strftime("%m-%y"))



print('Raw files Loading....')



d7=(datetime.now() - timedelta(7)).strftime('%d_%m_%Y')
d6=(datetime.now() - timedelta(6)).strftime('%d_%m_%Y')
d5=(datetime.now() - timedelta(5)).strftime('%d_%m_%Y')
d4=(datetime.now() - timedelta(4)).strftime('%d_%m_%Y')
d3=(datetime.now() - timedelta(3)).strftime('%d_%m_%Y')
d2=(datetime.now() - timedelta(2)).strftime('%d_%m_%Y')
d1=(datetime.now() - timedelta(1)).strftime('%d_%m_%Y')

d71=(datetime.now() - timedelta(7)).strftime('%Y%m%d')
d61=(datetime.now() - timedelta(6)).strftime('%Y%m%d')
d51=(datetime.now() - timedelta(5)).strftime('%Y%m%d')
d41=(datetime.now() - timedelta(4)).strftime('%Y%m%d')
d31=(datetime.now() - timedelta(3)).strftime('%Y%m%d')
d21=(datetime.now() - timedelta(2)).strftime('%Y%m%d')
d11=(datetime.now() - timedelta(1)).strftime('%Y%m%d')

dt7=(datetime.now() - timedelta(7)).strftime('%d-%b-%y')
dt6=(datetime.now() - timedelta(6)).strftime('%d-%b-%y')
dt5=(datetime.now() - timedelta(5)).strftime('%d-%b-%y')
dt4=(datetime.now() - timedelta(4)).strftime('%d-%b-%y')
dt3=(datetime.now() - timedelta(3)).strftime('%d-%b-%y')
dt2=(datetime.now() - timedelta(2)).strftime('%d-%b-%y')
dt1=(datetime.now() - timedelta(1)).strftime('%d-%b-%y')


print('Here I add one more Deletion code- to remove all files from Directory and their subdirectory')


path = r'Local_path'

for folder, subfolders,files in os.walk(path):
    for fl in files:
        if fl.endswith(".csv" )or fl.endswith('.xlsx'):
            path = os.path.join(folder, fl)
            os.remove(path)

print("All Old Raw Files Deleted!")


                                                            # ** Reports Uploading **   



print(" ** Reports Uploading start on BI Portal -->> /Remote_Path/** ")

print(" ** Uploading Start ** ")

ssh0=paramiko.SSHClient()
ssh0.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh0.connect(hostname='10.10.10.10',username='Root',password='Root',port=22)
sftp_client0=ssh0.open_sftp()


try:
    sftp_client0.chdir('\Remote_Path\')
    sftp_client0.put(r'local_Path\Report_Name_'+d7+'.csv','Report_Name_'+d7+'.csv')
    
except:
    pass


try:
    sftp_client0.chdir('\Remote_Path\')
    sftp_client0.put(r'local_Path\Report_Name_'+d6+'.csv','Report_Name_'+d6+'.csv')

except:
    pass


sftp_client0.close
ssh0.close


print(" ********* Congratulations All Report Successfully Uploaded *********** ")


print('This is a smaple code I deleted the rest of the code lines as all are same only file name changed')


