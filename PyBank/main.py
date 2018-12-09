# File Name: main.py
# Date: 12-08-2018
# Author: Zhen Yang
# Purpose: Analyze records in budget_data.csv and calculate the following:
# - The total number of months included in the dataset
# - The total net amount of "Profit/Losses" over the entire period
# - The average change in "Profit/Losses" between months over the entire period
# - The greatest increase in profits (date and amount) over the entire period
# - The greatest decrease in losses (date and amount) over the entire period

# Module for creating file paths across operating systems
import os

# Module for reading CSV files
import csv

# Initialize variables
total_month = 0
total_amount = 0
previous_amount = 0
current_change = 0
total_change = 0
average_change = 0
greatest_increase = 0
greatest_decrease = 0
greatest_increase_month = ""
greatest_decrease_month = ""

# Path for budget_data.csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Error handling 
try:

    # Open file
    with open(csvpath, newline='') as csvfile:

        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')

        # Skip the header row 
        csv_header = next(csvreader)
    
        # Loop though rows and do calculations
        # row[0] - Date
        # row[1] - Profit/Losses
        for row in csvreader:

            # Increment total month counter by 1
            total_month = total_month +1

            # Add up total amount
            total_amount = total_amount + int(row[1])

            # Calculate total change first. Do not have total number of months at this point.
            # Calculate average change after the loop.
            # Calculate from the 2nd month
            current_change = int(row[1]) - previous_amount
            if previous_amount != 0:
                total_change = total_change + current_change
            previous_amount = int(row[1])

            # Calculate greatest increase
            if current_change > greatest_increase:
                greatest_increase = current_change
                greatest_increase_month = row[0]

            # Calculate greatest decrease
            if (greatest_decrease > current_change):
                greatest_decrease = current_change
                greatest_decrease_month = row[0]

        # Calculate average change. Change starts from 2nd month. 
        # So total change should be divided by total number of months minus 1
        # Round the result to 2 places after decimal point
        # Error handling: if there is only 1 row of data, do not execute 
        # this line of code to avoid divide by 0 error
        if (total_month != 1): 
            average_change = round((total_change/(total_month -1)), 2)

        # Compose results
        result = "Financial Analysis \n"
        result = result + "------------------------------- \n"
        result = result + "Total Months: " + str(total_month) + "\n"
        result = result + "Total: " + str(total_amount) + "\n"
        result = result + "Average Change: $" + str(average_change) + "\n"
        result = result + "Greatest Increase in Profits: " + greatest_increase_month + " (" + str(round(greatest_increase, 0)) + ")\n"
        result = result + "Greatest Decrease in Profits: " + greatest_decrease_month + " (" + str(round(greatest_decrease, 0)) + ")\n"

        # Print result to terminal
        print(result)

        # Write to result.txt in Output folder.
        # If the folder does not exist, create the folder first
        if not os.path.exists("Output"):
            os.makedirs("Output")
        output_file = open("Output/result.txt", "w")
        output_file.write(result)
        output_file.close()

# Handle print or file error
except IOError as e:
   print("IO error: " + str(e))

# Handle system related error, such as mkdir error
except OSError as e:
    print("OS error: " + str(e))

# Handle other errors such as empty data file, wrong delimiter
except: 
   print("Unexpected error. Please check the data")