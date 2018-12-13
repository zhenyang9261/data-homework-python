# File Name: main.py
# Date: 12-10-2018
# Author: Zhen Yang
# Purpose: Convert format of the records in data file 
#  Original format: 214,Sarah Simpson,1985-12-04,111-11-1111,Florida
#  Convert to:
# - The Name column should be split into separate First Name and Last Name columns.
# - The DOB data should be re-written into MM/DD/YYYY format.
# - The SSN data should be re-written such that the first five numbers are hidden from view.
# - The State data should be re-written as simple two-letter abbreviations.

# Module for creating file paths across operating systems
import os

# Module for reading CSV files
import csv

# Import functions from the library file
from mylib import formatHeader, formatName, formatDate, formatSSN, formatState

# Path for data file
csvpath = os.path.join('Resources', 'employee_data.csv')

# Error handling 
try:

    # Open file
    with open(csvpath, newline='') as csvfile:

        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')

        # Read the header row 
        csv_header = next(csvreader)

        # Create output file
        if not os.path.exists("Output"):
            os.makedirs("Output")
        output_file = open("Output/new_employee_data.csv", "w")

        # Write header in result first
        new_header = formatHeader(str(csv_header))
        output_file.write(f"{new_header} \n")

        # Loop though rows and re-write content to new file
        for row in csvreader:

            # Convert name
            new_name = formatName(row[1])
            # Convert DOB
            new_date = formatDate(row[2]) 
            #Convert SSN
            new_ssn = formatSSN(row[3])
            # Convert state
            new_state = formatState(row[4])
           
            # Compose results
            output_file.write(f"{row[0]},{new_name},{new_date},{new_ssn},{new_state}\n")

# Handle print or file error
except IOError as e:
   print("IO error: " + str(e))

# Handle system related error, such as mkdir error
except OSError as e:
    print("OS error: " + str(e))

# Handle other errors such as empty data file, wrong delimiter
except: 
   print("Unexpected error. Please check the data")