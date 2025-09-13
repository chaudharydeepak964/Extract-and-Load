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

######################



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



files_asm = glob.glob(os.path.join(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ASM_I/*.csv'))
for file in files_asm:
    os.remove(file)

files_bih = glob.glob(os.path.join(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\BIH_I/*.csv'))
for file in files_bih:
    os.remove(file)

files_kar = glob.glob(os.path.join(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR/*.csv'))
for file in files_kar:
    os.remove(file)

files_odi = glob.glob(os.path.join(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ODI/*.csv'))
for file in files_odi:
    os.remove(file)

files_upe = glob.glob(os.path.join(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\UPE/*.csv'))
for file in files_upe:
    os.remove(file)

files_rob = glob.glob(os.path.join(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB/*.csv'))
for file in files_rob:
    os.remove(file)

print('Raw files Deleted....')


###############C:\TXN\RAW\CERA  Full_Link_Report_27_12_2022.csv   27_12_2022

ssh0=paramiko.SSHClient()
ssh0.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh0.connect(hostname='10.115.1.39',username='vodafone',password='Regional@#@#',port=22)
except:
    pass
try:
    ssh0.connect(hostname='10.19.62.239',username='vodafone',password='Regional@#@#',port=22)
except:
    pass

sftp_client0=ssh0.open_sftp()


sftp_client0.chdir('/opt/mycom/data/ceragon/microwave/csvascii_nr21/cm1/UPE' )

try:
    sftp_client0.get('Full_Link_Report_'+d7+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\UPE\Full_Link_Report_'+d7+'.csv')
except:
    pass

try:
    sftp_client0.get('Full_Link_Report_'+d6+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\UPE\Full_Link_Report_'+d6+'.csv')
except:
    pass

try:
    sftp_client0.get('Full_Link_Report_'+d5+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\UPE\Full_Link_Report_'+d5+'.csv')
except:
    pass

try:
    sftp_client0.get('Full_Link_Report_'+d4+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\UPE\Full_Link_Report_'+d4+'.csv')
except:
    pass

try:
    sftp_client0.get('Full_Link_Report_'+d3+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\UPE\Full_Link_Report_'+d3+'.csv')
except:
    pass

try:
    sftp_client0.get('Full_Link_Report_'+d2+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\UPE\Full_Link_Report_'+d2+'.csv')
except:
    pass

try:
    sftp_client0.get('Full_Link_Report_'+d1+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\UPE\Full_Link_Report_'+d1+'.csv')
except:
    pass


sftp_client0.chdir('/opt/mycom/data/ceragon/microwave/csvascii_nr21/pm1/Test_2/UPE' )

try:
    sftp_client0.get('Ethernet_Radio_Report_IP-20_24h_'+d7+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\UPE\Ethernet_Radio_Report_IP-20_24h_'+d7+'.csv')
except:
    pass

try:
    sftp_client0.get('Ethernet_Radio_Report_IP-20_24h_'+d6+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\UPE\Ethernet_Radio_Report_IP-20_24h_'+d6+'.csv')
except:
    pass

try:
    sftp_client0.get('Ethernet_Radio_Report_IP-20_24h_'+d5+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\UPE\Ethernet_Radio_Report_IP-20_24h_'+d5+'.csv')
except:
    pass

try:
    sftp_client0.get('Ethernet_Radio_Report_IP-20_24h_'+d4+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\UPE\Ethernet_Radio_Report_IP-20_24h_'+d4+'.csv')
except:
    pass

try:
    sftp_client0.get('Ethernet_Radio_Report_IP-20_24h_'+d3+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\UPE\Ethernet_Radio_Report_IP-20_24h_'+d3+'.csv')
except:
    pass

try:
    sftp_client0.get('Ethernet_Radio_Report_IP-20_24h_'+d2+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\UPE\Ethernet_Radio_Report_IP-20_24h_'+d2+'.csv')
except:
    pass

try:
    sftp_client0.get('Ethernet_Radio_Report_IP-20_24h_'+d1+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\UPE\Ethernet_Radio_Report_IP-20_24h_'+d1+'.csv')
except:
    pass


#############

sftp_client0.chdir('/opt/mycom/data/ceragon/microwave/csvascii_nr21/cm1/ROB' )

try:
    sftp_client0.get('Full_Link_Report_'+d7+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Full_Link_Report_'+d7+'.csv')
except:
    pass

try:
    sftp_client0.get('Full_Link_Report_'+d6+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Full_Link_Report_'+d6+'.csv')
except:
    pass

try:
    sftp_client0.get('Full_Link_Report_'+d5+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Full_Link_Report_'+d5+'.csv')
except:
    pass

try:
    sftp_client0.get('Full_Link_Report_'+d4+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Full_Link_Report_'+d4+'.csv')
except:
    pass

try:
    sftp_client0.get('Full_Link_Report_'+d3+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Full_Link_Report_'+d3+'.csv')
except:
    pass

try:
    sftp_client0.get('Full_Link_Report_'+d2+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Full_Link_Report_'+d2+'.csv')
except:
    pass

try:
    sftp_client0.get('Full_Link_Report_'+d1+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Full_Link_Report_'+d1+'.csv')
except:
    pass




sftp_client0.chdir('/opt/mycom/data/ceragon/microwave/csvascii_nr21/pm1/Test_2/ROB' )

try:
    sftp_client0.get('Ethernet_Radio_Report_IP-20_24h_'+d7+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Ethernet_Radio_Report_IP-20_24h_'+d7+'.csv')
except:
    pass

try:
    sftp_client0.get('Ethernet_Radio_Report_IP-20_24h_'+d6+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Ethernet_Radio_Report_IP-20_24h_'+d6+'.csv')
except:
    pass

try:
    sftp_client0.get('Ethernet_Radio_Report_IP-20_24h_'+d5+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Ethernet_Radio_Report_IP-20_24h_'+d5+'.csv')
except:
    pass

try:
    sftp_client0.get('Ethernet_Radio_Report_IP-20_24h_'+d4+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Ethernet_Radio_Report_IP-20_24h_'+d4+'.csv')
except:
    pass

try:
    sftp_client0.get('Ethernet_Radio_Report_IP-20_24h_'+d3+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Ethernet_Radio_Report_IP-20_24h_'+d3+'.csv')
except:
    pass

try:
    sftp_client0.get('Ethernet_Radio_Report_IP-20_24h_'+d2+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Ethernet_Radio_Report_IP-20_24h_'+d2+'.csv')
except:
    pass

try:
    sftp_client0.get('Ethernet_Radio_Report_IP-20_24h_'+d1+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Ethernet_Radio_Report_IP-20_24h_'+d1+'.csv')
except:
    pass



sftp_client0.chdir('/opt/mycom/data/ceragon/microwave/csvascii_nr21/pm1/ROB' )

try:
    sftp_client0.get('Radio_PM_Report_IP-20_24h_'+d7+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Radio_PM_Report_IP-20_24h_'+d7+'.csv')
except:
    pass

try:
    sftp_client0.get('Radio_PM_Report_IP-20_24h_'+d6+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Radio_PM_Report_IP-20_24h_'+d6+'.csv')
except:
    pass

try:
    sftp_client0.get('Radio_PM_Report_IP-20_24h_'+d5+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Radio_PM_Report_IP-20_24h_'+d5+'.csv')
except:
    pass

try:
    sftp_client0.get('Radio_PM_Report_IP-20_24h_'+d4+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Radio_PM_Report_IP-20_24h_'+d4+'.csv')
except:
    pass

try:
    sftp_client0.get('Radio_PM_Report_IP-20_24h_'+d3+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Radio_PM_Report_IP-20_24h_'+d3+'.csv')
except:
    pass

try:
    sftp_client0.get('Radio_PM_Report_IP-20_24h_'+d2+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Radio_PM_Report_IP-20_24h_'+d2+'.csv')
except:
    pass

try:
    sftp_client0.get('Radio_PM_Report_IP-20_24h_'+d1+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Radio_PM_Report_IP-20_24h_'+d1+'.csv')
except:
    pass



sftp_client0.chdir('/opt/mycom/data/ceragon/microwave/csvascii_nr21/cm1/KAR' )

try:
    sftp_client0.get('Full_Link_Report_'+d7+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\Full_Link_Report_'+d7+'.csv')
except:
    pass

try:
    sftp_client0.get('Full_Link_Report_'+d6+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\Full_Link_Report_'+d6+'.csv')
except:
    pass

try:
    sftp_client0.get('Full_Link_Report_'+d5+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\Full_Link_Report_'+d5+'.csv')
except:
    pass

try:
    sftp_client0.get('Full_Link_Report_'+d4+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\Full_Link_Report_'+d4+'.csv')
except:
    pass

try:
    sftp_client0.get('Full_Link_Report_'+d3+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\Full_Link_Report_'+d3+'.csv')
except:
    pass

try:
    sftp_client0.get('Full_Link_Report_'+d2+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\Full_Link_Report_'+d2+'.csv')
except:
    pass

try:
    sftp_client0.get('Full_Link_Report_'+d1+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\Full_Link_Report_'+d1+'.csv')
except:
    pass


sftp_client0.chdir('/opt/mycom/data/ceragon/microwave/csvascii_nr21/pm1/Test_2/KAR' )

try:
    sftp_client0.get('Ethernet_Radio_Report_IP-20_24h_'+d7+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\Ethernet_Radio_Report_IP-20_24h_'+d7+'.csv')
except:
    pass

try:
    sftp_client0.get('Ethernet_Radio_Report_IP-20_24h_'+d6+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\Ethernet_Radio_Report_IP-20_24h_'+d6+'.csv')
except:
    pass

try:
    sftp_client0.get('Ethernet_Radio_Report_IP-20_24h_'+d5+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\Ethernet_Radio_Report_IP-20_24h_'+d5+'.csv')
except:
    pass

try:
    sftp_client0.get('Ethernet_Radio_Report_IP-20_24h_'+d4+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\Ethernet_Radio_Report_IP-20_24h_'+d4+'.csv')
except:
    pass

try:
    sftp_client0.get('Ethernet_Radio_Report_IP-20_24h_'+d3+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\Ethernet_Radio_Report_IP-20_24h_'+d3+'.csv')
except:
    pass

try:
    sftp_client0.get('Ethernet_Radio_Report_IP-20_24h_'+d2+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\Ethernet_Radio_Report_IP-20_24h_'+d2+'.csv')
except:
    pass

try:
    sftp_client0.get('Ethernet_Radio_Report_IP-20_24h_'+d1+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\Ethernet_Radio_Report_IP-20_24h_'+d1+'.csv')
except:
    pass




sftp_client0.chdir('/opt/mycom/data/ceragon/microwave/csvascii_nr21/pm1/KAR' )

try:
    sftp_client0.get('Radio_PM_Report_IP-20_24h_'+d7+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\KRadio_PM_Report_IP-20_24h_'+d7+'.csv')
except:
    pass

try:
    sftp_client0.get('Radio_PM_Report_IP-20_24h_'+d6+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\KRadio_PM_Report_IP-20_24h_'+d6+'.csv')
except:
    pass

try:
    sftp_client0.get('Radio_PM_Report_IP-20_24h_'+d5+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\KRadio_PM_Report_IP-20_24h_'+d5+'.csv')
except:
    pass

try:
    sftp_client0.get('Radio_PM_Report_IP-20_24h_'+d4+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\KRadio_PM_Report_IP-20_24h_'+d4+'.csv')
except:
    pass

try:
    sftp_client0.get('Radio_PM_Report_IP-20_24h_'+d3+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\KRadio_PM_Report_IP-20_24h_'+d3+'.csv')
except:
    pass

try:
    sftp_client0.get('Radio_PM_Report_IP-20_24h_'+d2+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\KRadio_PM_Report_IP-20_24h_'+d2+'.csv')
except:
    pass

try:
    sftp_client0.get('Radio_PM_Report_IP-20_24h_'+d1+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\KRadio_PM_Report_IP-20_24h_'+d1+'.csv')
except:
    pass



sftp_client0.close
ssh0.close

print('Raw files downloaded')


## __________________________________________________________________________________________________________________________________________________________________##

## __________________________________________________________________________________________________________________________________________________________________##

## __________________________________________________________________________________________________________________________________________________________________##



print(' ** Files Uploading Start ** ')



ssh3=paramiko.SSHClient()
ssh3.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh3.connect(hostname='10.19.62.229',username='Cobra',password='Cobra@123',port=22)
except:
    pass
sftp_client1=ssh3.open_sftp()


sftp_client1.chdir('/opt/MyLog/TX/CERAGON_UTIL/KAR')


try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\Ethernet_Radio_Report_IP-20_24h_'+d1+'.csv', 'Ethernet_Radio_Report_IP-20_24h_'+d1+'.csv')
except:
    pass

try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\Ethernet_Radio_Report_IP-20_24h_'+d2+'.csv', 'Ethernet_Radio_Report_IP-20_24h_'+d2+'.csv')
except:
    pass

try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\Ethernet_Radio_Report_IP-20_24h_'+d3+'.csv', 'Ethernet_Radio_Report_IP-20_24h_'+d3+'.csv')
except:
    pass

try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\Ethernet_Radio_Report_IP-20_24h_'+d4+'.csv', 'Ethernet_Radio_Report_IP-20_24h_'+d4+'.csv')
except:
    pass

try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\Ethernet_Radio_Report_IP-20_24h_'+d5+'.csv', 'Ethernet_Radio_Report_IP-20_24h_'+d5+'.csv')
except:
    pass

try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\Ethernet_Radio_Report_IP-20_24h_'+d6+'.csv', 'Ethernet_Radio_Report_IP-20_24h_'+d6+'.csv')
except:
    pass

try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\Ethernet_Radio_Report_IP-20_24h_'+d7+'.csv', 'Ethernet_Radio_Report_IP-20_24h_'+d7+'.csv')
except:
    pass



try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\Full_Link_Report_'+d1+'.csv', 'Full_Link_Report_'+d1+'.csv')
except:
    pass

try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\Full_Link_Report_'+d2+'.csv', 'Full_Link_Report_'+d2+'.csv')
except:
    pass

try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\Full_Link_Report_'+d3+'.csv', 'Full_Link_Report_'+d3+'.csv')
except:
    pass

try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\Full_Link_Report_'+d4+'.csv', 'Full_Link_Report_'+d4+'.csv')
except:
    pass

try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\Full_Link_Report_'+d5+'.csv', 'Full_Link_Report_'+d5+'.csv')
except:
    pass

try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\Full_Link_Report_'+d6+'.csv', 'Full_Link_Report_'+d6+'.csv')
except:
    pass

try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\Full_Link_Report_'+d7+'.csv', 'Full_Link_Report_'+d7+'.csv')
except:
    pass

print ( " KAR Ethernet AND Full Link Uploaded on Cobra ")


sftp_client1.chdir('/opt/MyLog/TX/CERAGON_UTIL/ROB')


try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Ethernet_Radio_Report_IP-20_24h_'+d1+'.csv', 'Ethernet_Radio_Report_IP-20_24h_'+d1+'.csv')
except:
    pass

try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Ethernet_Radio_Report_IP-20_24h_'+d2+'.csv', 'Ethernet_Radio_Report_IP-20_24h_'+d2+'.csv')
except:
    pass

try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Ethernet_Radio_Report_IP-20_24h_'+d3+'.csv', 'Ethernet_Radio_Report_IP-20_24h_'+d3+'.csv')
except:
    pass
try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Ethernet_Radio_Report_IP-20_24h_'+d4+'.csv', 'Ethernet_Radio_Report_IP-20_24h_'+d4+'.csv')
except:
    pass

try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Ethernet_Radio_Report_IP-20_24h_'+d5+'.csv', 'Ethernet_Radio_Report_IP-20_24h_'+d5+'.csv')
except:
    pass

try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Ethernet_Radio_Report_IP-20_24h_'+d6+'.csv', 'Ethernet_Radio_Report_IP-20_24h_'+d6+'.csv')
except:
    pass

try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Ethernet_Radio_Report_IP-20_24h_'+d7+'.csv', 'Ethernet_Radio_Report_IP-20_24h_'+d7+'.csv')
except:
    pass




try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Full_Link_Report_'+d1+'.csv', 'Full_Link_Report_'+d1+'.csv')
except:
    pass

try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Full_Link_Report_'+d2+'.csv', 'Full_Link_Report_'+d2+'.csv')
except:
    pass

try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Full_Link_Report_'+d3+'.csv', 'Full_Link_Report_'+d3+'.csv')
except:
    pass

try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Full_Link_Report_'+d4+'.csv', 'Full_Link_Report_'+d4+'.csv')
except:
    pass

try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Full_Link_Report_'+d5+'.csv', 'Full_Link_Report_'+d5+'.csv')
except:
    pass

try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Full_Link_Report_'+d6+'.csv', 'Full_Link_Report_'+d6+'.csv')
except:
    pass

try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Full_Link_Report_'+d7+'.csv', 'Full_Link_Report_'+d7+'.csv')
except:
    pass

print ( " ROB Ethernet AND Full Link Uploaded on Cobra ")



sftp_client1.chdir('/opt/MyLog/TX/MW_availabilty_report/CERAGON')



try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Radio_PM_Report_IP-20_24h_'+d1+'.csv', 'Radio_PM_Report_IP-20_24h_'+d1+'.csv')
except:
    pass

try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Radio_PM_Report_IP-20_24h_'+d2+'.csv', 'Radio_PM_Report_IP-20_24h_'+d2+'.csv')
except:
    pass

try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Radio_PM_Report_IP-20_24h_'+d3+'.csv', 'Radio_PM_Report_IP-20_24h_'+d3+'.csv')
except:
    pass

try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Radio_PM_Report_IP-20_24h_'+d4+'.csv', 'Radio_PM_Report_IP-20_24h_'+d4+'.csv')
except:
    pass

try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Radio_PM_Report_IP-20_24h_'+d5+'.csv', 'Radio_PM_Report_IP-20_24h_'+d5+'.csv')
except:
    pass

try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Radio_PM_Report_IP-20_24h_'+d6+'.csv', 'Radio_PM_Report_IP-20_24h_'+d6+'.csv')
except:
    pass

try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Radio_PM_Report_IP-20_24h_'+d7+'.csv', 'Radio_PM_Report_IP-20_24h_'+d7+'.csv')
except:
    pass


try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\ROB\Full_Link_Report_'+d1+'.csv', 'RFull_Link_Report_'+d1+'.csv')
except:
    pass


print ( " ROB Radio AND Full Link Uploaded on Cobra for UAS ")



try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\KRadio_PM_Report_IP-20_24h_'+d1+'.csv', 'KRadio_PM_Report_IP-20_24h_'+d1+'.csv')
except:
    pass

try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\KRadio_PM_Report_IP-20_24h_'+d2+'.csv', 'KRadio_PM_Report_IP-20_24h_'+d2+'.csv')
except:
    pass

try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\KRadio_PM_Report_IP-20_24h_'+d3+'.csv', 'KRadio_PM_Report_IP-20_24h_'+d3+'.csv')
except:
    pass

try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\KRadio_PM_Report_IP-20_24h_'+d4+'.csv', 'KRadio_PM_Report_IP-20_24h_'+d4+'.csv')
except:
    pass

try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\KRadio_PM_Report_IP-20_24h_'+d5+'.csv', 'KRadio_PM_Report_IP-20_24h_'+d5+'.csv')
except:
    pass

try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\KRadio_PM_Report_IP-20_24h_'+d6+'.csv', 'KRadio_PM_Report_IP-20_24h_'+d6+'.csv')
except:
    pass

try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\KRadio_PM_Report_IP-20_24h_'+d7+'.csv', 'KRadio_PM_Report_IP-20_24h_'+d7+'.csv')
except:
    pass


try:
    sftp_client1.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\COBRA-RAW\KAR\Full_Link_Report_'+d1+'.csv', 'KFull_Link_Report_'+d1+'.csv')
except:
    pass


print ( " KAR Radio AND Full Link Uploaded on Cobra for UAS ")

sftp_client1.close
ssh3.close

print("Upload done")






