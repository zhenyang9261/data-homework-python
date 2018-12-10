# File Name: main.py
# Date: 12-08-2018
# Author: Zhen Yang
# Purpose: Analyze records in election_data.csv and calculate the following:
# - The total number of votes cast
# - A complete list of candidates who received votes
# - The percentage of votes each candidate won
# - The total number of votes each candidate won
# - The winner of the election based on popular vote.

# Module for creating file paths across operating systems
import os

# Module for reading CSV files
import csv

# Initialize variables
total_vote = 0
candidate_col = 2

# Dictionary of the result:
# key: candidate name
# value: total vote for this candidate
poll = {}

# Path for budget_data.csv file
csvpath = os.path.join('Resources', 'election_data.csv')

# Error handling 
try:

    # Open file
    with open(csvpath, newline='') as csvfile:

        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')

        # Skip the header row 
        csv_header = next(csvreader)
    
        # Loop though rows and do calculations
        for row in csvreader:

            # Increment total vote counter
            total_vote = total_vote + 1
            
            # If the key exists already, increment this key's value by 1
            # else, initialize this key's value
            if (row[candidate_col] in poll):
                poll[row[candidate_col]] = poll[row[candidate_col]] + 1
            else:
                poll[row[candidate_col]] = 1

        # Compose result string
        result = "Election Results \n"
        result = result + "--------------------------------- \n"
        result = result + f"Total Votes: {total_vote} \n"
        result = result + "--------------------------------- \n"

        # Compose result part of the result string
        # If data set empty, result is set to 'Data Set Empty'
        if total_vote != 0:
            
            # Calculate percent, round to 3 places after decimal point
            for key, value in poll.items():
                percent = "{0:.3f}".format(round(value/total_vote*100,3))
                result = result + f"{key}: {percent}%  ({value}) \n"         
            result = result + "--------------------------------- \n"

            # Find the winner. Return key (candidate name) of the max value
            v=list(poll.values())
            k=list(poll.keys())
            winner = k[v.index(max(v))]
            result = result + f"Winner: {winner} \n"

        else:
            result = result + "Data Set Empty \n"  
        
        result = result + "--------------------------------- \n"

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
   print("Unexpected error")