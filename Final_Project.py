#Hist and PIA
import os
import sys
import fileinput
import datetime
#Function to process VR
def VR_processing(QN_number,QN_date,QN_description,Material_number):
   # Create file name based on user input
   File_name = QN_number +" VR "+ QN_description+"."+"txt"
   # Copy the template contents to the file that was created above.
   with open('Template Hist and PIA.txt', 'r') as source_file, open(File_name, 'w') as dest_file:
    for line in source_file:
      dest_file.write(line.replace('VR: ; Initiated on: ; Material:', 'VR: ' + QN_number +'; Intiated on:' + QN_date + '; Material:' + Material_number))

#Function to process NC
#def NC_processing(QN_number,QN_date,QN_description,Material_number):
# Same as above processing but instead of VR, will use NC. 
   

# Get user inputs for QN_number, QN_date, QN_description and Material_number
QN_number = input("Enter the QN number: ")
QN_date = input("Enter the QN date: ")
QN_description = input("Enter QN description: ")
Material_number = input("Enter the Material number: ")

# If it's an VR
if len(QN_number) == 7:
   if QN_number[0] == '9':
      VR_processing(QN_number,QN_date,QN_description,Material_number)

# If it's a NC
   elif QN_number[0] == '4':
      #NC_processing(QN_number,QN_date,QN_description,Material_number)
      print("NC processing")

# If it's an invalid entry
   else:
      print("Invalid QN number entered!")
else:
   print("Invalid Entry!")
