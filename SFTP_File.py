print(" Ceragon Raw files upload on Cobra ")

from datetime import datetime, timedelta,date
import pandas as pd
import numpy as np
import paramiko
import os.path
from datetime import date 
from os import path
from glob import glob
import glob
import warnings
warnings.filterwarnings("ignore")

pd.set_option('display.float_format', '{:.2f}'.format)

d1=(datetime.now() - timedelta(3)).strftime('%m-%d-%Y')

de=((datetime.now() - timedelta(1)).strftime('%d-%m-%Y'))
de0=((datetime.now() - timedelta(0)).strftime('%d-%m-%Y'))

d=(datetime.now() - timedelta(1)).strftime('%d%m%Y')
dep=((datetime.now() - timedelta(1)).strftime("%d_%b'%Y"))
mnt=((datetime.now() - timedelta(0)).strftime("%m-%y"))


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



files_asm = glob.glob(os.path.join(r'Local_Path/*.csv'))
for file in files_asm:
    os.remove(file)

files_bih = glob.glob(os.path.join(r'Local_Path/*.csv'))
for file in files_bih:
    os.remove(file)

# You can add more code just change the path

print('Raw files Deleted....')

print('SFTP Started....')

ssh0=paramiko.SSHClient()
ssh0.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh0.connect(hostname='1.1.1.1',username='admin',password='admin',port=22)
except:
    pass
try:
    ssh0.connect(hostname='0.0.0.0',username='admin',password='admin',port=22)
except:
    pass

sftp_client0=ssh0.open_sftp()

print('Connection Stablished....')

sftp_client0.chdir('Server_Path1' )

try:
    sftp_client0.get('Report_Name_'+d7+'.csv',r'local_Path\Report_Name'+d7+'.csv')
except:
    pass

try:
    sftp_client0.get('Report_Name_'+d6+'.csv',r'local_Path\Report_Name'+d6+'.csv')
except:
    pass



sftp_client0.chdir('Server_Path2' )

try:
    sftp_client0.get('Report_Name_'+d7+'.csv',r'local_Path\Report_Name'+d7+'.csv')
except:
    pass

try:
    sftp_client0.get('Report_Name_'+d6+'.csv',r'local_Path\Report_Name'+d6+'.csv')
except:
    pass


sftp_client0.close
ssh0.close

print('Raw files downloaded on local Path')




