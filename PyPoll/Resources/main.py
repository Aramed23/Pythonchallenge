 # First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

election_data = os.path.join("Resources" ,"election_data.csv")

# Define variables 
candidate= []
number_votes= []
total_votes = 0
percent_votes = []
with open(election_data, newline = "") as csvfile:
 
 # CSV reader specifies delimiter and variable that holds contents
 csvreader = csv.reader(csvfile, delimiter=',')

# Read the header row first (skip this step if there is no header)
csv_header = next(csvreader)

 # Read each row of data after the header
for row in csvreader:
    # vote tracker for total votes
     total_votes= total_votes + 1
    # if candidate is not in the list, then add it and with their vote. If candidate is already in the list then add a vote
if row[2] not in candidate:
     candidate.append(row[2])
     index= candidate.index(row[2])
     number_votes.append(1)
    
else:
    index = candidate.index(row[2])
    number_votes.index= number_votes.index+(1)

# add percent to the list 
for votes in number_votes:
     percent= (votes/total_votes)* 100
     percent = round(percent,2)
     percent_votes.append(percent)

  # finding out the winner 
     winner = max(number_votes) 
     index = number_votes. index(winner)
     win_candidate = candidate[index]


print("Election Results\n")
print("----------------------------\n")
print(f"Total Votes : {total_votes}")
print("----------------------------\n")
print(f"Charles Casper Stockham:{str(percent_votes)} ({str(number_votes)}")
print(f"Diana DeGette:{str(percent_votes)} ({str(number_votes)}")     
print(f"Raymon Anthony Doane:{str(percent_votes)} ({str(number_votes)}")
print("----------------------------\n")
print(f"winner: {win_candidate}") 
