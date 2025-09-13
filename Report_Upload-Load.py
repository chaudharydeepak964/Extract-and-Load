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


                                   ###########   *********************** CM DOWNLAODING  ***********************  #############




print(" ** CM Files downloading start ** ")

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


#################  ASM_I  ##################



#################  UPE  ##################

sftp_client0.chdir('/opt/mycom/data/ceragon/microwave/csvascii_nr21/cm1/UPE' )

try:
    sftp_client0.get('Full_Link_Report_'+d1+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\CM\TXN_CERA_UPE_Full_Link_Report_'+d1+'.csv')
except:
    pass

try:
    sftp_client0.get('Network_Element_Report_'+d1+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\CM\TXN_CERA_UPE_Network_Element_Report_'+d1+'.csv')
except:
    pass


#################  ROB  ##################

sftp_client0.chdir('/opt/mycom/data/ceragon/microwave/csvascii_nr21/cm1/ROB' )

try:
    sftp_client0.get('Full_Link_Report_'+d1+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\CM\TXN_CERA_ROB_Full_Link_Report_'+d1+'.csv')
except:
    pass

try:
    sftp_client0.get('Network_Element_Report_'+d1+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\CM\TXN_CERA_ROB_Network_Element_Report_'+d1+'.csv')
except:
    pass



#################  KAR  ##################


sftp_client0.chdir('/opt/mycom/data/ceragon/microwave/csvascii_nr21/cm1/KAR' )

try:
    sftp_client0.get('Full_Link_Report_'+d1+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\CM\TXN_CERA_KAR_Full_Link_Report_'+d1+'.csv')
except:
    pass

try:
    sftp_client0.get('Network_Element_Report_'+d1+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\CM\TXN_CERA_KAR_Network_Element_Report_'+d1+'.csv')
except:
    pass

print(" ** 12 CM Files downloaded ** ")





                                   ###########   *********************** PM DOWNLAODING  ***********************  #############







print(" ** PM Files downloading start ** ")
      
#################  UPE  ##################

sftp_client0.chdir('/opt/mycom/data/ceragon/microwave/csvascii_nr21/pm1/UPE')

try:
    sftp_client0.get('Radio_PM_Report_IP-10_24h_'+d1+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\PM\TXN_CERA_UPE_Radio_PM_Report_IP-10_24h_'+d1+'.csv')
except:
    pass

try:
    sftp_client0.get('Radio_PM_Report_IP-20_24h_'+d1+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\PM\TXN_CERA_UPE_Radio_PM_Report_IP-20_24h_'+d1+'.csv')
except:
    pass

try:
    sftp_client0.get('Ethernet_Radio_Report_IP-10_24h_'+d1+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\PM\TXN_CERA_UPE_Ethernet_Radio_Report_IP-10_24h_'+d1+'.csv')
except:
    pass

try:
    sftp_client0.get('Ethernet_Radio_Report_IP-20_24h_'+d1+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\PM\TXN_CERA_UPE_Ethernet_Radio_Report_IP-20_24h_'+d1+'.csv')
except:
    pass

try:
    sftp_client0.get('Ethernet_Utilization_Report_24h_'+d1+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\PM\TXN_CERA_UPE_Ethernet_Utilization_Report_24h_'+d1+'.csv')
except:
    pass


#################  KAR  ##################


sftp_client0.chdir('/opt/mycom/data/ceragon/microwave/csvascii_nr21/pm1/KAR' )


try:
    sftp_client0.get('Radio_PM_Report_IP-20_24h_'+d1+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\PM\TXN_CERA_KAR_Radio_PM_Report_IP-20_24h_'+d1+'.csv')
except:
    pass


try:
    sftp_client0.get('Ethernet_Radio_Report_IP-20_24h_'+d1+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\PM\TXN_CERA_KAR_Ethernet_Radio_Report_IP-20_24h_'+d1+'.csv')
except:
    pass

try:
    sftp_client0.get('Ethernet_Utilization_Report_24h_'+d1+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\PM\TXN_CERA_KAR_Ethernet_Utilization_Report_24h_'+d1+'.csv')
except:
    pass


#################  ROB  ##################


sftp_client0.chdir('/opt/mycom/data/ceragon/microwave/csvascii_nr21/pm1/ROB' )


try:
    sftp_client0.get('Radio_PM_Report_IP-20_24h_'+d1+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\PM\TXN_CERA_ROB_Radio_PM_Report_IP-20_24h_'+d1+'.csv')
except:
    pass


try:
    sftp_client0.get('Ethernet_Radio_Report_IP-20_24h_'+d1+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\PM\TXN_CERA_ROB_Ethernet_Radio_Report_IP-20_24h_'+d1+'.csv')
except:
    pass

try:
    sftp_client0.get('Radio_PM_Report_IP-10_24h_'+d1+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\PM\TXN_CERA_ROB_Radio_PM_Report_IP-10_24h_'+d1+'.csv')
except:
    pass


try:
    sftp_client0.get('Ethernet_Radio_Report_IP-10_24h_'+d1+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\PM\TXN_CERA_ROB_Ethernet_Radio_Report_IP-10_24h_'+d1+'.csv')
except:
    pass

try:
    sftp_client0.get('Ethernet_Utilization_Report_24h_'+d1+'.csv',r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\PM\TXN_CERA_ROB_Ethernet_Utilization_Report_24h_'+d1+'.csv')
except:
    pass





sftp_client0.close
ssh0.close

print(" ** 21 PM Files downloaded ** ")




                                                            # ** Reports Uploading **   



print(" ** Reports Uploading start on BI Portal -->> /home/snenrc/VIL_IDEA_REPORTS/TX_REPORT ** ")

print(" ** CM Uploading Start ** ")

ssh0=paramiko.SSHClient()
ssh0.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh0.connect(hostname='10.19.33.41',username='snenrc',password='Qwer!234',port=22)
sftp_client0=ssh0.open_sftp()


###############  FULL LINK  ################

try:
    sftp_client0.chdir('/home/snenrc/VIL_IDEA_REPORTS/TX_REPORT')
    sftp_client0.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\CM\TXN_CERA_UPE_Full_Link_Report_'+d1+'.csv','TXN_CERA_UPE_Full_Link_Report_'+d1+'.csv')
    
except:
    pass


try:
    sftp_client0.chdir('/home/snenrc/VIL_IDEA_REPORTS/TX_REPORT')
    sftp_client0.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\CM\TXN_CERA_KAR_Full_Link_Report_'+d1+'.csv','TXN_CERA_KAR_Full_Link_Report_'+d1+'.csv')
    
except:
    pass

try:
    sftp_client0.chdir('/home/snenrc/VIL_IDEA_REPORTS/TX_REPORT')
    sftp_client0.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\CM\TXN_CERA_ROB_Full_Link_Report_'+d1+'.csv','TXN_CERA_ROB_Full_Link_Report_'+d1+'.csv')
    
except:
    pass





print(" ** FULL LINK UPLOADED ** ")



#############  NETOWRK ELEMENT  ##############

try:
    sftp_client0.chdir('/home/snenrc/VIL_IDEA_REPORTS/TX_REPORT')
    sftp_client0.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\CM\TXN_CERA_UPE_Network_Element_Report_'+d1+'.csv','TXN_CERA_UPE_Network_Element_Report_'+d1+'.csv')
    
except:
    pass

try:
    sftp_client0.chdir('/home/snenrc/VIL_IDEA_REPORTS/TX_REPORT')
    sftp_client0.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\CM\TXN_CERA_KAR_Network_Element_Report_'+d1+'.csv','TXN_CERA_KAR_Network_Element_Report_'+d1+'.csv')
    
except:
    pass

try:
    sftp_client0.chdir('/home/snenrc/VIL_IDEA_REPORTS/TX_REPORT')
    sftp_client0.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\CM\TXN_CERA_ROB_Network_Element_Report_'+d1+'.csv','TXN_CERA_ROB_Network_Element_Report_'+d1+'.csv')
    
except:
    pass


print(" ** NETOWRK ELEMENT UPLOADED ** ")


print(" ** PM Uploading Start ** ")

#################  UPE  ##################

try:
    sftp_client0.chdir('/home/snenrc/VIL_IDEA_REPORTS/TX_REPORT')
    sftp_client0.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\PM\TXN_CERA_UPE_Radio_PM_Report_IP-10_24h_'+d1+'.csv','TXN_CERA_UPE_Radio_PM_Report_IP-10_24h_'+d1+'.csv')
    
except:
    pass


try:
    sftp_client0.chdir('/home/snenrc/VIL_IDEA_REPORTS/TX_REPORT')
    sftp_client0.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\PM\TXN_CERA_UPE_Radio_PM_Report_IP-20_24h_'+d1+'.csv','TXN_CERA_UPE_Radio_PM_Report_IP-20_24h_'+d1+'.csv')
    
except:
    pass


try:
    sftp_client0.chdir('/home/snenrc/VIL_IDEA_REPORTS/TX_REPORT')
    sftp_client0.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\PM\TXN_CERA_UPE_Ethernet_Radio_Report_IP-10_24h_'+d1+'.csv','TXN_CERA_UPE_Ethernet_Radio_Report_IP-10_24h_'+d1+'.csv')
    
except:
    pass

try:
    sftp_client0.chdir('/home/snenrc/VIL_IDEA_REPORTS/TX_REPORT')
    sftp_client0.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\PM\TXN_CERA_UPE_Ethernet_Radio_Report_IP-20_24h_'+d1+'.csv','TXN_CERA_UPE_Ethernet_Radio_Report_IP-20_24h_'+d1+'.csv')
    
except:
    pass

try:
    sftp_client0.chdir('/home/snenrc/VIL_IDEA_REPORTS/TX_REPORT')
    sftp_client0.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\PM\TXN_CERA_UPE_Ethernet_Utilization_Report_24h_'+d1+'.csv','TXN_CERA_UPE_Ethernet_Utilization_Report_24h_'+d1+'.csv')
    
except:
    pass


print(" ** UPE PM UPLOADED ** ")

#################  KAR  ##################


try:
    sftp_client0.chdir('/home/snenrc/VIL_IDEA_REPORTS/TX_REPORT')
    sftp_client0.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\PM\TXN_CERA_KAR_Radio_PM_Report_IP-20_24h_'+d1+'.csv','TXN_CERA_KAR_Radio_PM_Report_IP-20_24h_'+d1+'.csv')
    
except:
    pass



try:
    sftp_client0.chdir('/home/snenrc/VIL_IDEA_REPORTS/TX_REPORT')
    sftp_client0.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\PM\TXN_CERA_KAR_Ethernet_Radio_Report_IP-20_24h_'+d1+'.csv','TXN_CERA_KAR_Ethernet_Radio_Report_IP-20_24h_'+d1+'.csv')
    
except:
    pass

try:
    sftp_client0.chdir('/home/snenrc/VIL_IDEA_REPORTS/TX_REPORT')
    sftp_client0.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\PM\TXN_CERA_KAR_Ethernet_Utilization_Report_24h_'+d1+'.csv','TXN_CERA_KAR_Ethernet_Utilization_Report_24h_'+d1+'.csv')
    
except:
    pass

print(" ** KAR PM UPLOADED ** ")


#################  ROB ##################



try:
    sftp_client0.chdir('/home/snenrc/VIL_IDEA_REPORTS/TX_REPORT')
    sftp_client0.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\PM\TXN_CERA_ROB_Radio_PM_Report_IP-20_24h_'+d1+'.csv','TXN_CERA_ROB_Radio_PM_Report_IP-20_24h_'+d1+'.csv')
    
except:
    pass



try:
    sftp_client0.chdir('/home/snenrc/VIL_IDEA_REPORTS/TX_REPORT')
    sftp_client0.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\PM\TXN_CERA_ROB_Ethernet_Radio_Report_IP-20_24h_'+d1+'.csv','TXN_CERA_ROB_Ethernet_Radio_Report_IP-20_24h_'+d1+'.csv')
    
except:
    pass


try:
    sftp_client0.chdir('/home/snenrc/VIL_IDEA_REPORTS/TX_REPORT')
    sftp_client0.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\PM\TXN_CERA_ROB_Radio_PM_Report_IP-10_24h_'+d1+'.csv','TXN_CERA_ROB_Radio_PM_Report_IP-10_24h_'+d1+'.csv')
    
except:
    pass



try:
    sftp_client0.chdir('/home/snenrc/VIL_IDEA_REPORTS/TX_REPORT')
    sftp_client0.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\PM\TXN_CERA_ROB_Ethernet_Radio_Report_IP-10_24h_'+d1+'.csv','TXN_CERA_ROB_Ethernet_Radio_Report_IP-10_24h_'+d1+'.csv')
    
except:
    pass

try:
    sftp_client0.chdir('/home/snenrc/VIL_IDEA_REPORTS/TX_REPORT')
    sftp_client0.put(r'C:\Users\COR1736664\Desktop\Deepak\ALL CODE\All_Report_BI_Push\Ceragon\RAW\PM\TXN_CERA_ROB_Ethernet_Utilization_Report_24h_'+d1+'.csv','TXN_CERA_ROB_Ethernet_Utilization_Report_24h_'+d1+'.csv')
    
except:
    pass


print(" ** ROB PM UPLOADED ** ")


sftp_client0.close
ssh0.close



print(" ********* Congratulations All Report Successfully Uploaded *********** ")



