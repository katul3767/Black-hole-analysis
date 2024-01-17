#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 12:38:56 2023

@author: atul
"""

import csv
import matplotlib.pyplot as plt
import pandas as pd
import csv
import numpy as np

# The black hole candidates
with open("1A 0620-00.csv", 'r') as file:
#with open("4U 1543-475.csv", 'r') as file:  
#with open("4U 1630-472.csv", 'r') as file: 
#with open("4U 1957+115.csv", 'r') as file: 
#with open("AT 2019wey.csv", 'r') as file:
#with open("Cyg.X-1.csv", 'r') as file:
#with open("EXO 1722-363.csv", 'r') as file:
#with open("EXO 1846-031.csv", 'r') as file:
#with open("GRS 1915+105.csv", 'r') as file:
#with open("GS 1354-64.csv", 'r') as file:
#with open("GX 339-4.csv", 'r') as file:
#with open("H 1743-322.csv", 'r') as file:
#with open("MAXI J1803-298.csv", 'r') as file:
#with open("SLX 1746-331.csv", 'r') as file:
#with open("GS 2000+251.csv", 'r') as file:
#with open("Swift J1753.5-0127.csv", 'r') as file:
#with open("V404 Cyg.csv", 'r') as file:
#with open("GS 2000+251.csv", 'r') as file:
#with open("GS 2000+251.csv", 'r') as file:
#with open("GS 2000+251.csv", 'r') as file:

#with open("output.csv", 'r') as file:   #Fairall 9, GRS 1739-278


    csvreader = csv.reader(file,delimiter="\t")
    for row in csvreader:
           
                col1_data = []
                col2_data = []
                col3_data = []
                col4_data = []
                col5_data = []
                col6_data = []
                col7_data = []
                col8_data = []
                col9_data = []
                
            # Loop through the rows in the CSV file
                for row in csvreader:
                    col1_data.append(float(row[0]))
                    col2_data.append(float(row[1]))
                    col3_data.append(float(row[2]))
                    col4_data.append(float(row[3]))
                    col5_data.append(float(row[4]))
                    col6_data.append(float(row[5])) 
                    col7_data.append(float(row[6]))
                    col8_data.append(float(row[7]))
                    col9_data.append(float(row[8]))
                    
# columns with heading                    
MJDcenter, 2-20keV, err ,2-4keV, err ,4-10keV ,err ,10-20keV, err     

# naming the data from the csv formatted file
MJDcenter = np.array(col1_data)
twotwentykeV = np.array(col2_data)
error1 = np.array(col3_data)
twofourkeV= np.array(col4_data)
error2= np.array(col5_data)
fourtenkeV= np.array(col6_data)
error3= np.array(col7_data)
tentwentykeV= np.array(col8_data)
error4= np.array(col9_data
                 
# error propagation 
# (A/B)*(r_A+r_B)  .................(1)
# where r_A and r_B is given as r_A = error_A/A , r_B = error_B/B
# error associated with A

r_A1 = np.array(error3)/np.array(fourtenkeV)

# similarly, the error associated with B
r_B1= np.array(error2)/np.array(twofourkeV)

div1=fourtenkeV/twofourkeV

# error propagation
fourtenvstwofour=(fourtenkeV/twofourkeV)*(r_A1+r_B1)

# error associated with A
r_A2 = np.array(error4)/np.array(tentwentykeV)

# similarly, the error associated with B
r_B2= np.array(error2)/np.array(twofourkeV)
# error propagation
tentwntyvstwofour=(tentwentykeV/twofourkeV)*(r_A2+r_B2)

div2=tentwentykeV/twofourkeV     
                 
fig = plt.figure(0,(14,14))
plt.title('title ')
plt.subplot(2, 2, 1)
plt.errorbar(MJDcenter,twotwentykeV, yerr=error1,fmt='.g');
plt.xlabel('Time [MJD]')
plt.ylabel('2-20keV[ph/s/cm2]')
plt.title('4U 1957+115')

plt.subplot(2, 2, 2)
plt.errorbar(MJDcenter,div1, yerr=fourtenvstwofour,fmt='.k')
plt.xlabel('Time [MJD]')
plt.ylabel('4-10keV/2-4keV [ph/s/cm2]')
#plt.title('4-10keV/2-4keV [ph/s/cm2]'
#plt.errorbar(MJDcenter,fourtenvstwofour, yerr=error1, fmt='.k');

plt.xlabel('Time [MJD]')
plt.ylabel('4-10keV/2-4keV [ph/s/cm2]')
#plt.title('4-10keV/2-4keV [ph/s/cm2]')

plt.subplot(2, 2, 3)
plt.errorbar(MJDcenter,div2, yerr=tentwntyvstwofour,fmt='.r')
plt.xlabel('Time [MJD]')
plt.ylabel('10-20keV/2-4keV [ph/s/cm2]')
#plt.title('10-20keV/2-4keV [ph/s/cm2]')

plt.subplot(2, 2, 4)
plt.errorbar(div1,div2,yerr=tentwntyvstwofour,xerr=fourtenvstwofour,            
            fmt='o')
plt.xlabel('4-10/2-4)keV [ph/s/cm2]')
plt.ylabel('10-20/2-4)keV [ph/s/cm2]')
#plt.title('10-20keV/2-4keV [ph/s/cm2]')
plt.show()                